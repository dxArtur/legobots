from ev3dev2.button import Button

# Cria uma instância dos botões
btn = Button()

# Aguarda até que o botão "enter" seja pressionado
print("Pressione o botão 'enter' para continuar...")
btn.wait_for_bump('enter')
print("Botão 'enter' pressionado!")