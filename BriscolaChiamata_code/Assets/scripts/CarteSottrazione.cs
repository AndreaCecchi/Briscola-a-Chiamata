using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CarteSottrazione : MonoBehaviour
{
    public static List<Carta> Carte = new List<Carta>();
    public static void Add(Carta c)
    {
        Carte.Add(c);
    }
    public static void Remove(Carta c)
    {
        Carta carta = Carte.Find(x => x.figura == c.figura && x.seme == c.seme);
        Carte.Remove(carta);
    }
    public static int Count()
    {
        return Carte.Count;
    }
}
