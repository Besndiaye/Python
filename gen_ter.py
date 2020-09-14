# def intervalle(borne_inf, borne_sup):
#     """Générateur parcourant la série des entiers entre borne_inf et borne_sup.
    
#     Note: borne_inf doit être inférieure à borne_sup"""
    
#     borne_inf += 1
#     while borne_inf < borne_sup:
#         yield borne_inf
#         borne_inf += 1


def custtom_range(n):
    for i in range(1, n +1):
        yield i

# generateur = custtom_range(10)
# for i in generateur:
#     print(i)
for i in custtom_range(20):
    print(i)