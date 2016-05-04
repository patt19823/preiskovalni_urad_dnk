#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

lasje_crna = "CCAGCAATCGC"
lasje_rjava =  "GCCAGTGCCG"
lasje_korencek = "TTAGCTATCGC"

obraz_kvadraten = "GCCACGG"
obraz_okrogel = "ACCACAA"
obraz_ovalen = "AGGCCTCA"

oci_modra = "TTGTGGTGGC"
oci_zelena = "GGGAGGTGGC"
oci_rjava = "AAGTAGTGAC"

spol_moski = "TGCAGGAACTTC"
spol_zenska = "TGAAGGACCTTC"

rasa_Belec = "AAAACCTCA"
rasa_crnec = "CGACTACAG"
rasa_azijec = "CGCGGGCCG"

class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

    def post(self):
        dnk_code = self.request.get("dnk_code")

        if (lasje_crna in str(dnk_code)):
            barva_las = "Crna"
        elif (lasje_rjava in str(dnk_code)):
            barva_las = "Rjava"
        elif (lasje_korencek in str(dnk_code)):
            barva_las = "Korencek"
        else:
            barva_las ="Neznana"

        if (obraz_okrogel in str(dnk_code)):
            oblika_obraza = " Okrogla"
        elif (obraz_kvadraten in str(dnk_code)):
            oblika_obraza = "Kvadratna"
        elif (obraz_ovalen in str(dnk_code)):
            oblika_obraza = " Ovalna"
        else:
            oblika_obraza = "Nepoznana"

        if (oci_modra in str(dnk_code)):
            barva_oci = "Modra"
        elif (oci_rjava in str(dnk_code)):
            barva_oci = "Rjava"
        elif (oci_zelena in str(dnk_code)):
            barva_oci = "Zelena"
        else:
            barva_oci ="Neznana"

        if (spol_moski in str(dnk_code)):
            spol = "Moski"
        elif (spol_zenska in str(dnk_code)):
            spol = "Zenksa"
        else:
            spol ="Neznan"

        if (rasa_Belec in str(dnk_code)):
            rasa = "Belec"
        elif (rasa_azijec in str(dnk_code)):
            rasa = "Azijec"
        elif (rasa_crnec in str(dnk_code)):
            rasa = "Crnec"
        else:
            rasa ="Neznana"


        view_vars = {
            "barva_las": barva_las,
            "oblika_obraza": oblika_obraza,
            "barva_oci": barva_oci,
            "spol": spol,
            "rasa": rasa,
        }
        return self.render_template("dnk.html", view_vars)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
