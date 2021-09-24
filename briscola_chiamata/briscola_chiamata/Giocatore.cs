using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace briscola_chiamata
{
    class Giocatore
    {
        public string nome;
        public int posizione;
        public bool flagChiamante;
        public int puntiVittoria;
        private Carta[] carteInMano = new Carta[8];
        private bool[] mano = new bool[8];
        private Carta[] prese = new Carta[5];
        private int[] probChiamato = new int[8];

        public Giocatore(string aNome, int aPosizione)
        {
            nome = aNome;
            posizione = aPosizione;
        }
    }
}
