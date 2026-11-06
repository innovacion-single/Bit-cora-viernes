"""Genera index.html (solo lectura) a partir de plantilla.html y datos.json."""
import json, sys, datetime, pathlib
aqui = pathlib.Path(__file__).parent
datos = json.loads((aqui / "datos.json").read_text(encoding="utf-8"))
MES = ["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"]
hoy = datetime.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else datetime.date.today()
fecha = f"{hoy.day} {MES[hoy.month-1]} {hoy.year}"
js = json.dumps(datos, ensure_ascii=False).replace("</", "<\\/")
html = (aqui / "plantilla.html").read_text(encoding="utf-8")
html = html.replace("/*__DATA__*/[]", js).replace("/*__FECHA__*/", fecha)
(aqui / "index.html").write_text(html, encoding="utf-8")
print("index.html generado:", len(datos), "proyectos,", fecha)
