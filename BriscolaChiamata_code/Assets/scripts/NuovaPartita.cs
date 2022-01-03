using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class NuovaPartita : MonoBehaviour
{
    public void NewGame()
    {
        SceneManager.LoadScene("MenuGiocatore");
    }
}
