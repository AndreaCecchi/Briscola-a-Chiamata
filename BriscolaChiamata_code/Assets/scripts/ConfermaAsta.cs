using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class ConfermaAsta : MonoBehaviour
{
   
    public void Conferma(){

        bool ok=true;
        Partita.puntVittoria = System.Int16.Parse(GameObject.FindWithTag("punteggiochiamato").GetComponent<InputField>().text);
        if (Partita.puntVittoria < 61 || Partita.puntVittoria > 120)
            ok = false;
        if (GameObject.FindWithTag("nomeChiamante").GetComponent<InputField>().text != Partita.listagiocatori[0].nome && GameObject.FindWithTag("nomeChiamante").GetComponent<InputField>().text != Partita.listagiocatori[1].nome && GameObject.FindWithTag("nomeChiamante").GetComponent<InputField>().text != Partita.listagiocatori[2].nome && GameObject.FindWithTag("nomeChiamante").GetComponent<InputField>().text != Partita.listagiocatori[3].nome)
            ok = false;
        foreach (Giocatore x in Partita.listagiocatori)
        {
            if (x.nome == GameObject.FindWithTag("nomeChiamante").GetComponent<InputField>().text)
            {
                x.flagChiamante = true;
                
            }
        }
        Partita.cartachiamata = new Carta(System.Int16.Parse(GameObject.FindWithTag("figurachiamata").GetComponent<InputField>().text), GameObject.FindWithTag("semechiamato").GetComponent<Dropdown>().options[GameObject.FindWithTag("semechiamato").GetComponent<Dropdown>().value].text);
        if (Partita.cartachiamata.figura < 1 || Partita.cartachiamata.figura > 10)
            ok = false;
        if (ok)
        {
            foreach (Giocatore g in Partita.listagiocatori)
                if (g.flagChiamante)
                    print("ha chiamato " + g.nome + " in posizione " + g.posizione + " a " + Partita.puntVittoria + " punti\n");
            print("la carta chiamata è " + Partita.cartachiamata.figura + " di " + Partita.cartachiamata.seme);

            //Partita.listagiocatori.Find(x => x.flagChiamante == true).carteInMano.Add(Partita.cartachiamata);//mette in mano al chiamante la carta chiamata

            for (int i = 1; i < 11; i++)
            {
                Partita.briscoleInGioco.Add(new Carta(i, Partita.cartachiamata.seme));
            }


            foreach (Giocatore g in Partita.listagiocatori)
            {
                foreach (Carta x in g.carteInMano)
                {
                    if (x.figura == Partita.cartachiamata.figura && x.seme == Partita.cartachiamata.seme)
                    {
                        g.flagChiamato = true;
                    }

                }
            }

            SceneManager.LoadScene("TurnoGioco");
        }
        else
        {
            print("informazioni inserite non valide, inserirle di nuovo");
            GameObject.FindWithTag("figurachiamata").GetComponent<InputField>().text = null;
            GameObject.FindWithTag("punteggiochiamato").GetComponent<InputField>().text = null;
            GameObject.FindWithTag("nomeChiamante").GetComponent<InputField>().text = null;
        }
    }
}
