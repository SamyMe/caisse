
class caisse(object):
    
    def __init__(self, catalogue_file="test_data/catalogue.csv"):
        self.catalogue_file=catalogue_file
        self.catalogue = {}
        self._lire_catalogue()


    def _lire_catalogue(self,):
        """ Lecture du fichier contenant les produits.
            Le fichier est donné en argument lors de la 
            creation de l'instance de la classe. 
        """

        print('\n* Lecture du catalogue...')
        with open(self.catalogue_file, 'r') as cat_file:
            produit = ''
            prix = ''
            for row in cat_file.readlines():
                try:
                    produit, prix = row.rstrip().split(',')
                    # Pour faciliter la comparaison
                    produit = produit.lower()

                    if produit in self.catalogue: 
                        # Produit dupliqué
                        raise KeyError
                    else:
                        # Introduire au catalogue
                        self.catalogue[produit] = float(prix)

                except ValueError:
                    print("[ERREUR CATALOGUE]: Erreure de format dans: {}".format(row))
                except KeyError:
                    print("[ERREUR CATALOGUE]: Produit '{}' dupliqué!".format(produit))


    def calculate_total(self,):
        
        print('\n* Début de saisie...')
        print("""
                Veuillez entrer les produits sous la forme:
                NomDuProduit  NombreDeKilo
                et taper fin pour terminer la saisie.
               """)

        end_saisie = False
        total_achat = 0
        i = 1

        # Boucler sur l'introduction des articles
        while not end_saisie==True:
            saisie = input('Article n°{}: '.format(i))

            if 'fin' == saisie.lower():
                end_saisie = True
                print("Total: {:.2f}€".format(total_achat))
            else:
                saisie = saisie.split(',')

                try:

                    produit = saisie[0]
                    quantite = saisie[1]
                    prix = self.catalogue[produit]

                    total_achat += float(quantite)*prix 

                except ValueError:
                    print("[ERREUR]: Quantité mal introduite!!")
                except IndexError:
                    print("[ERREUR]: Saisie erronée!")
                except KeyError:
                    print("[ERREUR]: Produit inconue!")

            i += 1


if __name__ == "__main__":
    c = caisse()
    c.calculate_total()
