class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_rascal = Restaurante()
restaurante_rascal.nome = 'Rascal'
restaurante_rascal.categoria = 'Mediterraneo'
restaurante_rascal.ativo = False


restaurante_sukyia = Restaurante()

restaurantes = [restaurante_sukyia, restaurante_rascal]

print(restaurante_rascal.nome)