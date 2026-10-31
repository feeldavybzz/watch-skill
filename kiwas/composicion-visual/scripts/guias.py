#!/usr/bin/env python3
"""Guías de composición como geometría relativa (0..1) y su adaptación a cada formato.

Cada guía es una lista de primitivas en coordenadas relativas al cuadro (u a la derecha, v hacia abajo):
  {"t":"line","p":[[u,v],[u,v]]}   {"t":"poly","p":[[u,v],...],"closed":bool}   {"t":"dot","p":[u,v]}
Una guía se calcula para un formato concreto (ancho, alto): así las reglas de adaptación (por
orientación y proporción) viven en un solo sitio y el plugin las lee ya resueltas.

Origen: las 8 guías de la sección «reel» salen del reel de @jxframes (dibujadas sobre fotos 3:2); la
geometría estándar (tercios, áurea, espiral) es conocida. Los trazos libres (marco, líneas guía,
curva S) son valores por defecto editables, no medidas.

Uso:
  python guias.py --json SALIDA.json          # todas las guías resueltas para todos los formatos
  python guias.py --svg DIR                   # un SVG por guía y formato
  python guias.py --preview HOJA.png          # hoja de comprobación (necesita Pillow)
"""
import argparse, json, math, os, sys

PHI = (1 + 5 ** 0.5) / 2
G1, G2 = 1 / (PHI ** 2), 1 / PHI          # 0.382, 0.618

# nombre: (ancho, alto) de referencia en píxeles
FORMATOS = {"2.39:1": (1920, 803), "16:9": (1920, 1080), "3:2": (1620, 1080), "4:3": (1440, 1080), "5:4": (1350, 1080), "1:1": (1080, 1080),
            "4:5": (1080, 1350), "3:4": (1080, 1440), "2:3": (1080, 1620), "9:16": (1080, 1920)}
ORIGEN_REEL = "3:2 (reel 1, sobre lienzo 9:16) y 4:3 a pantalla completa (reels 2 y 3)"

ZONAS_SEGURAS = {   # 9:16, fracciones del alto/ancho. No oficial: fuentes de terceros discrepan.
    "9:16": {"ajustada": {"arriba": 0.13, "abajo": 0.13, "lados": 0.06},
             "conservadora": {"arriba": 0.14, "abajo": 0.35, "lados": 0.06, "riel_derecho": 0.21},
             "nota": "No oficial (fuentes de terceros); el margen inferior va de ≈250 a ≈670 px en 1080×1920. Probar en el móvil."}}


def orient(w, h):
    r = w / h
    return "horizontal" if r > 1.05 else "vertical" if r < 0.95 else "cuadrado"


def L(a, b): return {"t": "line", "p": [list(a), list(b)]}
def P(pts, closed=False): return {"t": "poly", "p": [list(p) for p in pts], "closed": closed}
def D(p): return {"t": "dot", "p": list(p)}


def r3(x): return round(x, 4)


# ---------------------------------------------------------------- espiral áurea
def _espiral_canonica(n_arcos=9, pasos=22):
    """Espiral en un rectángulo φ×1 (primer cuadrado a la izquierda). Devuelve (puntos, ojo)."""
    p, h, r = (0.0, 0.0), (0.0, 1.0), 1.0
    pts = []
    for k in range(n_arcos):
        hn = (h[1], -h[0])
        c = (p[0] + r * hn[0], p[1] + r * hn[1])
        for i in range(pasos + 1):
            th = (math.pi / 2) * i / pasos
            # c + r*( -hn*cos + h*sin )
            q = (c[0] + r * (-hn[0] * math.cos(th) + h[0] * math.sin(th)),
                 c[1] + r * (-hn[1] * math.cos(th) + h[1] * math.sin(th)))
            if not (k and i == 0): pts.append(q)
        p = (c[0] + r * h[0], c[1] + r * h[1]); h = hn; r /= PHI
    eye = p
    for _ in range(60):   # límite de la sucesión: el «ojo»
        hn = (h[1], -h[0]); c = (p[0] + r * hn[0], p[1] + r * hn[1])
        p = (c[0] + r * h[0], c[1] + r * h[1]); h = hn; r /= PHI
    return pts, p


_ESP, _OJO = _espiral_canonica()


def espiral(w, h, flipx=False, flipy=False, modo=None):
    """modo 'proporcional' (rectángulo áureo 1:1,618 completo, centrado, con márgenes) o 'estirada' (rellena el cuadro).
    Por defecto proporcional, salvo que la proporción esté a ±5 % de φ (o 1/φ). Evidencia: StudioBinder dibuja la espiral sobre
    un rectángulo áureo de 1,62:1 centrado en un cuadro 16:9, con ≈7 % de margen a cada lado (no estirado)."""
    a = w / h
    cerca = abs(a - PHI) / PHI < 0.05 or abs(1 / a - PHI) / PHI < 0.05
    modo = modo or ("estirada" if cerca else "proporcional")
    vertical = a < 1
    pts = [(x / PHI, y) for x, y in _ESP]; ojo = (_OJO[0] / PHI, _OJO[1])   # u,v en el rectángulo áureo horizontal
    if vertical:   # rotar 90° para que el lado largo del rectángulo áureo sea el vertical
        pts = [(y, x) for x, y in pts]; ojo = (ojo[1], ojo[0])
    if modo == "proporcional":   # escalar uniforme para que quepa, pegado arriba/izquierda
        rw, rh = (PHI, 1.0) if not vertical else (1.0, PHI)
        k = min(w / rw, h / rh) * 0.944   # px por unidad; 0,944 = lo medido en StudioBinder (rectángulo áureo algo menor que el cuadro)
        sx, sy = k * rw / w, k * rh / h    # fracción del cuadro que ocupa el rectángulo áureo
        ox, oy = (1 - sx) / 2, (1 - sy) / 2   # centrado
        pts = [(ox + x * sx, oy + y * sy) for x, y in pts]; ojo = (ox + ojo[0] * sx, oy + ojo[1] * sy)
    if flipx: pts = [(1 - x, y) for x, y in pts]; ojo = (1 - ojo[0], ojo[1])
    if flipy: pts = [(x, 1 - y) for x, y in pts]; ojo = (ojo[0], 1 - ojo[1])
    return [P([(r3(x), r3(y)) for x, y in pts]), D((r3(ojo[0]), r3(ojo[1])))], {"modo": modo, "ojo": [r3(ojo[0]), r3(ojo[1])]}


# ---------------------------------------------------------------- guías
def g_tercios(w, h):
    pts = [(u, v) for u in (1 / 3, 2 / 3) for v in (1 / 3, 2 / 3)]
    prim = [L((1 / 3, 0), (1 / 3, 1)), L((2 / 3, 0), (2 / 3, 1)), L((0, 1 / 3), (1, 1 / 3)), L((0, 2 / 3), (1, 2 / 3))]
    prim += [D(p) for p in pts]
    return prim, {"etiquetas_diagonal": [[1 / 6, 1 / 6], [0.5, 0.5], [5 / 6, 5 / 6]], "etiquetas_fila_central": [[1 / 6, 0.5], [0.5, 0.5], [5 / 6, 0.5]], "nota": "la etiqueta va en las celdas: en diagonal (reel 1) o en la fila central (reel 2)"}


def g_aurea(w, h):
    prim = [L((G1, 0), (G1, 1)), L((G2, 0), (G2, 1)), L((0, G1), (1, G1)), L((0, G2), (1, G2))]
    return prim, {}


def g_espiral(w, h):
    prim, meta = espiral(w, h, flipx=True, flipy=True)   # ojo abajo a la izquierda, como en el reel
    meta["orientaciones"] = "4 (voltear horizontal y vertical)"
    return prim, meta


def g_triangulos_metodo(w, h):
    """Dos diagonales de esquina a esquina y las perpendiculares desde las otras dos esquinas (método de las diagonales)."""
    prim = [L((0, 1), (1, 0)), L((0, 0), (1, 1))]
    ang = math.degrees(math.atan2(h, w))
    # perpendicular a la diagonal BL→TR desde la esquina TL y desde BR (en píxeles, luego a relativas)
    def perp(corner, a, b):
        ax, ay, bx, by = a[0] * w, a[1] * h, b[0] * w, b[1] * h
        dx, dy = bx - ax, by - ay; t = ((corner[0] * w - ax) * dx + (corner[1] * h - ay) * dy) / (dx * dx + dy * dy)
        return ((ax + t * dx) / w, (ay + t * dy) / h)
    f1, f2 = perp((0, 0), (0, 1), (1, 0)), perp((1, 1), (0, 1), (1, 0))
    prim += [L((0, 0), f1), L((1, 1), f2)]
    return prim, {"angulo_diagonal_grados": round(ang, 1), "nota": "el ángulo cambia con la proporción: 16:9 ≈29°, 3:2 ≈34°, 9:16 ≈61° respecto a la horizontal"}


def g_diagonales(w, h):
    """La del reel: una diagonal larga de esquina inferior a superior y otra corta que la corta formando una «<»."""
    v_fin = 0.12
    pend = (v_fin - 1.0)            # v = 1 + pend*u
    u_corte = 0.34
    prim = [L((0, 1), (1, v_fin)), L((0, 0.52), (u_corte, r3(1 + pend * u_corte)))]
    return prim, {"invertible": True, "nota": "elementos a lo largo de una diagonal; se puede invertir (espejo horizontal). En vertical se mantiene la pendiente relativa y sube más rápido en píxeles."}


def g_lineas_guia(w, h):
    """Dos líneas que llevan desde el borde inferior al punto de interés (cruce de tercios superior derecho): una recta y una curva."""
    obj = (2 / 3, 1 / 3)
    ini_recta = (0.05, 1.0)
    ini_curva = (0.30, 1.0) if orient(w, h) != "vertical" else (0.20, 1.0)
    # curva cúbica explícita
    c0, c1, c2, c3 = ini_curva, (ini_curva[0] + 0.02, 0.72), (obj[0] - 0.30, 0.50), obj
    curva = []
    for i in range(25):
        t = i / 24
        curva.append((r3((1 - t) ** 3 * c0[0] + 3 * (1 - t) ** 2 * t * c1[0] + 3 * (1 - t) * t ** 2 * c2[0] + t ** 3 * c3[0]),
                      r3((1 - t) ** 3 * c0[1] + 3 * (1 - t) ** 2 * t * c1[1] + 3 * (1 - t) * t ** 2 * c2[1] + t ** 3 * c3[1])))
    return [L(ini_recta, obj), P(curva), D(obj)], {"objetivo": list(map(r3, obj)), "nota": "puntos editables; más largas en vertical (más recorrido)"}


def g_punto_fuga(w, h):
    v = 0.5 if orient(w, h) != "vertical" else G1   # en vertical el punto sube a la línea áurea superior: más suelo para las líneas
    vp = (0.5, v)
    abajo = [0.20, 0.36, 0.50, 0.64, 0.80]
    prim = [L(vp, (u, 1.0)) for u in abajo] + [L(vp, (0.46, 0.0)), L(vp, (0.54, 0.0))] + [D(vp)]
    return prim, {"punto": list(vp), "nota": "en horizontal al centro; en vertical sube a 0,382. Movible."}


def g_centrado(w, h):
    a = 0.035
    prim = [L((0.5 - a, 0), (0.5 - a, 1)), L((0.5 + a, 0), (0.5 + a, 1))]
    return prim, {"banda": r3(2 * a), "nota": "dos líneas verticales alrededor del eje; ancho ≈7 % del ancho del cuadro; añadir eje horizontal opcional"}


def g_yuxtaposicion(w, h):
    if orient(w, h) == "vertical":
        return [L((0, 0.5), (1, 0.5))], {"eje": "horizontal", "nota": "en vertical se divide arriba/abajo; alternativa 0,382/0,618"}
    return [L((0.5, 0), (0.5, 1))], {"eje": "vertical", "nota": "en horizontal y cuadrado se divide izquierda/derecha (≈0,51 en el reel); alternativa 0,382/0,618"}


def g_espacio_negativo(w, h):
    """Región vacía que se enmarca: en el reel, el 65 % superior del cuadro con el sujeto en el tercio inferior."""
    v = 0.65 if orient(w, h) != "vertical" else 0.60
    return [P([(0.0, 0.0), (1.0, 0.0), (1.0, v), (0.0, v)], True)], {"region_vacia_v": v, "sujeto": "en la franja inferior", "nota": "el sujeto ocupa el tercio inferior; en reels 9:16 el pie queda bajo la interfaz: subir el sujeto o reducir la región"}


def g_primer_plano(w, h):
    """Línea ondulada que separa el primer plano (flores, hojas) del fondo."""
    v = 0.667 if orient(w, h) != "vertical" else 0.72
    pts = [(r3(i / 96), r3(v + 0.014 * math.sin(i * 0.22) + 0.007 * math.sin(i * 0.57 + 1))) for i in range(97)]
    return [P(pts)], {"linea_v": v, "nota": "ocupa el tercio inferior (≈0,667); en vertical ≈0,72; la forma es libre"}


def g_simetria(w, h):
    return [L((0.5, 0), (0.5, 1))], {"eje": "vertical", "nota": "eje único al centro (reflejo izquierda/derecha); para reflejos en agua añadir eje horizontal en v = 0,5"}


def g_contorno_sujeto(w, h):
    """Silueta del sujeto centrada (en el reel, una montaña): polígono libre, se calca sobre el sujeto real."""
    pts = [(0.225, 0.47), (0.31, 0.38), (0.40, 0.29), (0.47, 0.265), (0.50, 0.26), (0.53, 0.265), (0.60, 0.30), (0.69, 0.38), (0.77, 0.46), (0.50, 0.50)]
    k = 1.0 if orient(w, h) != "vertical" else 1.45   # en vertical el sujeto ocupa más del ancho
    s = 1080 * (k * w / 1920) / h   # escala uniforme en píxeles respecto a la silueta canónica en 16:9
    pts = [(r3(0.5 + (x - 0.5) * k), r3(0.40 + (y - 0.40) * s)) for x, y in pts]
    return [P(pts, True)], {"etiqueta_debajo": [0.5, 0.58], "nota": "silueta de ejemplo, centrada; ancho ≈55 % del cuadro (≈80 % en vertical); se edita punto a punto sobre el sujeto"}


def g_marco_circular(w, h):
    """Marco circular tipo puerta lunar con base: círculo de ≈48 % del ancho (horizontal) o 76 % (vertical)."""
    k = 0.24 if orient(w, h) != "vertical" else 0.38
    r_px = min(k * w, 0.42 * h)   # que el círculo quepa siempre en el cuadro
    cx, cy = 0.5, 0.45
    pts = [(r3(cx + (r_px * math.cos(2 * math.pi * i / 72)) / w), r3(cy + (r_px * math.sin(2 * math.pi * i / 72)) / h)) for i in range(73)]
    return [P(pts, True)], {"radio_fraccion_del_ancho": k, "nota": "círculo con el radio calculado en píxeles; si sale del cuadro bajar el centro o reducir el radio"}


def g_lineas_convergentes(w, h):
    """Dos curvas que parten del borde inferior y convergen en el centro (un camino que se aleja)."""
    ap = (0.5, 0.78 if orient(w, h) != "vertical" else 0.62)
    prim = []
    for u0 in (0.23, 0.77):
        pts = []
        for i in range(25):
            s = i / 24
            u = (1 - s) ** 2 * u0 + 2 * (1 - s) * s * (u0 + (ap[0] - u0) * 0.35) + s ** 2 * ap[0]
            v = (1 - s) ** 2 * 1.0 + 2 * (1 - s) * s * (1.0 - (1.0 - ap[1]) * 0.15) + s ** 2 * ap[1]
            pts.append((r3(u), r3(v)))
        prim.append(P(pts))
    return prim, {"vertice": list(ap), "nota": "camino que se aleja al centro; en vertical el vértice sube (más recorrido)"}


def g_linea_aurea_horizonte(w, h):
    """Línea horizontal a 0,382 de la altura: lugar ideal para los ojos del sujeto o el horizonte (StudioBinder)."""
    return [L((0, G1), (1, G1))], {"linea_v": r3(G1), "alternativa_v": r3(G2), "nota": "tomar la altura del cuadro y trazar 1:1,618; vale igual en cualquier proporción"}


def g_headroom_lookroom(w, h):
    """Ojos en la línea áurea, sujeto a 0,382 del lado opuesto a la mirada; la región delante es el lookroom."""
    prim = [L((0, G1), (1, G1)), L((G1, 0), (G1, 1)), D((G1, G1)), P([(G1, 0.05), (0.97, 0.05), (0.97, 0.95), (G1, 0.95)], True)]
    return prim, {"ojos_v": r3(G1), "sujeto_u": r3(G1), "region": "lookroom (espacio delante de la mirada)", "espejo": "si el sujeto mira a la izquierda, usar u = 0,618", "nota": "headroom mínimo; más espacio delante que detrás"}


def g_marco(w, h):
    o = orient(w, h)
    if o == "horizontal":   # polígono del reel (aprox.), editable
        pts = [(0.0, 0.58), (0.07, 0.56), (0.58, 0.10), (0.87, 0.15), (0.68, 0.99), (0.0, 0.99)]
        return [P(pts, True)], {"variante": "polígono del reel (≈)", "nota": "se calca sobre la abertura de cada foto"}
    m = 0.08 * min(w, h)   # margen en píxeles, igual en los cuatro lados
    mu, mv = m / w, m / h
    return [P([(mu, mv), (1 - mu, mv), (1 - mu, 1 - mv), (mu, 1 - mv)], True)], {"variante": "rectángulo con margen 8 % del lado corto", "nota": "en vertical y cuadrado un marco libre se arma sobre la abertura real"}


def g_triangulos(w, h):
    return g_triangulos_metodo(w, h)


def g_piramide(w, h):
    return [P([(0.5, 0.08), (0.95, 0.92), (0.05, 0.92)], True)], {"nota": "vértice arriba al centro, base abajo"}


def g_v(w, h):
    vp = (0.5, 0.45)
    return [L((0.05, 1.0), vp), L((0.95, 1.0), vp), D(vp)], {"nota": "dos líneas que parten de abajo y convergen sobre el horizonte"}


def g_radial(w, h):
    c = (0.5, 0.5); n = 12
    prim = []
    for i in range(n):
        ang = 2 * math.pi * i / n
        dx, dy = math.cos(ang), math.sin(ang)
        t = min((0.5 / abs(dx)) if abs(dx) > 1e-9 else 9, (0.5 / abs(dy)) if abs(dy) > 1e-9 else 9)
        prim.append(L(c, (r3(0.5 + dx * t), r3(0.5 + dy * t))))
    return prim + [D(c)], {"nota": "rayos desde un punto; punto y número movibles; puede haber varios"}


def g_curva_s(w, h):
    pts = []
    for i in range(41):
        t = i / 40
        v = 1 - t
        u = 0.5 + 0.28 * math.sin(2 * math.pi * t) * (1 - 0.3 * t)
        pts.append((r3(u), r3(v)))
    return [P(pts)], {"nota": "forma libre; amplitud mayor en vertical si hay recorrido"}


def g_l(w, h):
    return [P([(0.12, 0.08), (0.12, 0.88), (0.92, 0.88)])], {"nota": "horizonte a lo largo del trazo horizontal y un elemento en primer plano en la esquina"}


GUIAS = {
    # --- las 8 del reel (+ tercios y espiral con su fórmula estándar)
    "espiral_aurea": (g_espiral, "reel+estándar"), "marco_en_el_marco": (g_marco, "reel"),
    "tercios": (g_tercios, "reel+estándar"), "yuxtaposicion": (g_yuxtaposicion, "reel"),
    "diagonales": (g_diagonales, "reel"), "lineas_guia": (g_lineas_guia, "reel"),
    "punto_de_fuga": (g_punto_fuga, "reel"), "centrado": (g_centrado, "reel"),
    "linea_aurea_horizonte": (g_linea_aurea_horizonte, "StudioBinder"), "headroom_lookroom": (g_headroom_lookroom, "StudioBinder"),
    # --- reels 2 y 3 (4:3)
    "espacio_negativo": (g_espacio_negativo, "reel 2"), "primer_plano": (g_primer_plano, "reel 3"),
    "simetria": (g_simetria, "reels 2 y 3"), "contorno_del_sujeto": (g_contorno_sujeto, "reel 2"),
    "marco_circular": (g_marco_circular, "reel 3"), "lineas_convergentes": (g_lineas_convergentes, "reel 3"),
    # --- de la clase de arte y estándar
    "rejilla_aurea": (g_aurea, "estándar"), "triangulos": (g_triangulos, "clase de arte"),
    "piramide": (g_piramide, "clase de arte"), "v": (g_v, "clase de arte"), "radial": (g_radial, "clase de arte"),
    "curva_s": (g_curva_s, "clase de arte"), "l": (g_l, "clase de arte"),
}
REEL14 = ["espacio_negativo", "primer_plano", "simetria", "contorno_del_sujeto", "marco_circular", "lineas_convergentes"]
REEL8 = ["espiral_aurea", "marco_en_el_marco", "tercios", "yuxtaposicion", "diagonales", "lineas_guia", "punto_de_fuga", "centrado"]


def resolver(nombre, fmt):
    w, h = FORMATOS[fmt]
    fn, origen = GUIAS[nombre]
    prim, meta = fn(w, h)
    meta = dict(meta); meta["origen"] = origen
    return {"formato": fmt, "ancho": w, "alto": h, "orientacion": orient(w, h), "primitivas": prim, "meta": meta}


def en_area_segura(res, zona="ajustada"):
    """Reubica una guía ya resuelta dentro del área útil de un formato con interfaz encima (reels 9:16).
    u' = lados + u*(1 - 2*lados);  v' = arriba + v*(1 - arriba - abajo). Las guías se siguen definiendo sobre el cuadro
    completo (es el video real); esta capa es opcional y es de la plataforma, no de la composición."""
    z = ZONAS_SEGURAS.get(res["formato"], {}).get(zona)
    if not z: return res
    a, b, c = z["arriba"], z["abajo"], z["lados"]
    def m(q): return [r3(c + q[0] * (1 - 2 * c)), r3(a + q[1] * (1 - a - b))]
    prim = []
    for p in res["primitivas"]:
        q = dict(p); q["p"] = m(p["p"]) if p["t"] == "dot" else [m(x) for x in p["p"]]; prim.append(q)
    out = dict(res); out["primitivas"] = prim; out["area"] = zona
    return out


def todo():
    return {
        "version": 1,
        "formato_de_referencia_del_reel": ORIGEN_REEL,
        "coordenadas": "relativas al cuadro: u de izquierda a derecha, v de arriba abajo, 0..1",
        "formatos": {k: {"ancho": v[0], "alto": v[1], "orientacion": orient(*v)} for k, v in FORMATOS.items()},
        "zonas_seguras": ZONAS_SEGURAS,
        "reglas_de_adaptacion": REGLAS,
        "guias": {n: {f: resolver(n, f) for f in FORMATOS} for n in GUIAS},
    }


REGLAS = [
    "Tercios y rejilla áurea: líneas en 1/3, 2/3 (0,382 y 0,618) de cada eje; valen igual en cualquier proporción. Un horizonte va sobre la línea horizontal superior o inferior de los tercios; dos personajes, uno a cada lado de las intersecciones.",
    "Espiral áurea: el lado largo del rectángulo áureo sigue el lado largo del cuadro (en vertical se gira 90°). Por defecto modo «proporcional» (rectángulo 1:1,618 entero y centrado, con márgenes: así lo dibuja StudioBinder sobre 16:9, ≈7 % por lado); modo «estirada» (rellena el cuadro) solo si la proporción está a ±5 % de φ o por elección del usuario. Siempre 4 orientaciones (ojo en cualquier esquina).",
    "Las guías se calculan sobre el área de imagen, sin barras negras: un plano 2,39:1 dentro de un 16:9 usa la proporción 2,39:1 (en el triángulo áureo los pies de las perpendiculares cambian de ≈0,24 en 16:9 a ≈0,153 en 2,35:1; medido sobre un plano de *Pulp Fiction* y reproducido por `triangulos`).",
    "Diagonales y triángulos: de esquina a esquina; el ángulo cambia con la proporción (29° en 16:9, 61° en 9:16) y las perpendiculares se recalculan en píxeles.",
    "Yuxtaposición: línea vertical en horizontal y cuadrado; línea horizontal en vertical (4:5, 2:3, 9:16). Variante 0,382/0,618.",
    "Punto de fuga: al centro en horizontal; en vertical sube a 0,382 para dar más suelo a las líneas.",
    "Centrado: banda de ≈7 % del ancho alrededor del eje vertical; eje horizontal opcional.",
    "Marco dentro del marco: polígono libre calcado sobre la abertura; por defecto un rectángulo con margen del 8 % del lado corto; variante circular (puerta lunar) con radio calculado en píxeles.",
    "Espacio negativo: región vacía del 65 % superior (60 % en vertical) con el sujeto en la franja inferior; en reels 9:16 el pie queda bajo la interfaz.",
    "Primer plano: línea ondulada en el tercio inferior (≈0,667; ≈0,72 en vertical).",
    "Simetría: eje vertical al centro; en reflejos añadir eje horizontal. Contorno del sujeto: silueta editable centrada.",
    "Líneas convergentes: dos curvas desde el borde inferior al centro; en vertical el vértice sube.",
    "Líneas guía: del borde inferior al punto de interés (cruce de tercios superior derecho por defecto), recta y curva editables.",
    "Todo lo libre (marco, líneas guía, curva S, radial) son valores por defecto movibles, no medidas.",
    "Los formatos verticales (4:5, 3:4, 2:3, 9:16) comparten las mismas reglas geométricas; lo que distingue al 9:16 es la interfaz de la plataforma encima, que es una capa aparte (zonas seguras, `en_area_segura`) y no cambia la composición.",
    "Las reglas son por familia de proporción (horizontal, cuadrado, vertical), no por formato; el plugin detecta la familia con la proporción del proyecto y permite forzar otra por guía.",
    "Al cambiar de formato, recalcular la guía con la proporción nueva; no estirar los píxeles de la guía anterior.",
]


# ---------------------------------------------------------------- salida
def svg(res, stroke="#fff", fondo="#000", ancho_trazo=2.0):
    w, h = res["ancho"], res["alto"]
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">',
           f'<rect width="{w}" height="{h}" fill="{fondo}"/>']
    for p in res["primitivas"]:
        if p["t"] == "line":
            (a, b), (c, d) = p["p"]
            out.append(f'<line x1="{a*w:.1f}" y1="{b*h:.1f}" x2="{c*w:.1f}" y2="{d*h:.1f}" stroke="{stroke}" stroke-width="{ancho_trazo}" stroke-linecap="round"/>')
        elif p["t"] == "poly":
            pts = " ".join(f"{x*w:.1f},{y*h:.1f}" for x, y in p["p"])
            tag = "polygon" if p.get("closed") else "polyline"
            out.append(f'<{tag} points="{pts}" fill="none" stroke="{stroke}" stroke-width="{ancho_trazo}" stroke-linejoin="round" stroke-linecap="round"/>')
        elif p["t"] == "dot":
            out.append(f'<circle cx="{p["p"][0]*w:.1f}" cy="{p["p"][1]*h:.1f}" r="{max(w,h)*0.006:.1f}" fill="{stroke}"/>')
    out.append("</svg>")
    return "\n".join(out)


def preview(path, nombres, formatos=("16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "9:16"), celda=210, titulo=True):
    from PIL import Image, ImageDraw
    pad = 8; lab = 118 if titulo else 0
    W = lab + len(formatos) * (celda + pad); H = 24 + len(nombres) * (celda + pad)
    im = Image.new("RGB", (W, H), (28, 28, 28)); d = ImageDraw.Draw(im)
    for j, f in enumerate(formatos): d.text((lab + j * (celda + pad) + 4, 6), f, fill=(190, 255, 120))
    for i, n in enumerate(nombres):
        y0 = 24 + i * (celda + pad); d.text((6, y0 + celda // 2 - 6), n, fill=(230, 230, 230))
        for j, f in enumerate(formatos):
            r = resolver(n, f); w, h = r["ancho"], r["alto"]; k = celda / max(w, h)
            tw, th = int(w * k), int(h * k); x0 = lab + j * (celda + pad) + (celda - tw) // 2; y1 = y0 + (celda - th) // 2
            d.rectangle([x0, y1, x0 + tw, y1 + th], fill=(0, 0, 0), outline=(70, 70, 70))
            def xy(u, v): return (x0 + u * tw, y1 + v * th)
            for p in r["primitivas"]:
                if p["t"] == "line": d.line([xy(*p["p"][0]), xy(*p["p"][1])], fill=(255, 255, 255), width=1)
                elif p["t"] == "poly":
                    pts = [xy(*q) for q in p["p"]] + ([xy(*p["p"][0])] if p.get("closed") else [])
                    d.line(pts, fill=(255, 255, 255), width=1)
                elif p["t"] == "dot":
                    x, y = xy(*p["p"]); d.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(255, 220, 60))
    im.save(path)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json"); ap.add_argument("--svg"); ap.add_argument("--preview"); ap.add_argument("--solo", help="lista separada por comas")
    a = ap.parse_args()
    nombres = a.solo.split(",") if a.solo else list(GUIAS)
    if a.json:
        json.dump(todo(), open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print("OK", a.json)
    if a.svg:
        for n in nombres:
            for f in FORMATOS:
                d = os.path.join(a.svg, f.replace(":", "x")); os.makedirs(d, exist_ok=True)
                open(os.path.join(d, n + ".svg"), "w", encoding="utf-8").write(svg(resolver(n, f)))
        print("OK", a.svg)
    if a.preview:
        preview(a.preview, nombres); print("OK", a.preview)
