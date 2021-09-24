using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace briscola_chiamata
{
    class Carta
    {
        public string figura;
        public string seme;
        public int valore;

        public Carta(string aFigura, string aSeme)
        {
            figura = aFigura;
            seme = aSeme;
            if (figura == "asso")
                valore = 11;
            if (figura == "tre")
                valore = 10;
            if (figura == "re")
                valore = 4;
            if (figura == "donna")
                valore = 3;
            if (figura == "fante")
                valore = 2;
            else
                valore = 0;
        }
    }
}
