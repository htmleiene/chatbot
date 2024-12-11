import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw


# Função para criar bordas arredondadas
def create_rounded_rectangle(w, h, radius, color):
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((0, 0, w, h), radius, fill=color)
    return ImageTk.PhotoImage(img)

# Função para gerar respostas
def get_bot_response(message):
    message = message.lower()
    if "produto" in message or "item" in message:
        return "Pode me informar o nome ou código do produto? Assim, verifico as informações para você."
    elif "entrega" in message or "frete" in message:
        return "Informe seu CEP para calcularmos o frete e o prazo de entrega!"
    elif "pagamento" in message or "forma de pagamento" in message:
        return "Aceitamos cartão, PIX e boleto. Qual a forma de pagamento que você prefere usar?"
    elif "troca" in message or "devolução" in message:
        return "Sinto muito que algo não tenha saído como esperado! Vou te ajudar com a troca ou devolução. Por favor, envie o número do pedido para continuarmos."
    elif "obrigado" in message or "valeu" in message:
        return "Por nada! Estamos sempre aqui para ajudar. 😊"
    elif "tchau" in message or "até logo" in message:
        return "Tchau! Volte sempre! Foi um prazer ajudar você. 🛍️"
    else:
        return "Desculpe, não entendi. Pode reformular sua pergunta?"

# Função para enviar mensagem
def send_message():
    user_message = user_input.get().strip()
    if not user_message:
        return
    # Adiciona mensagem do usuário
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"Usuário:\n{user_message}\n", "user")
    response, button_text = get_bot_response(user_message)

    # Adiciona resposta do bot
    chat_log.insert(tk.END, f"Suporte ChatBot:\n{response}\n", "bot")
    if button_text:
        add_button(button_text)
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)
    user_input.delete(0, tk.END)


# Adiciona botão de ação no chat
def add_button(text):
    action_button = tk.Button(chat_log, text=text, bg="#1976d2", fg="white", font=("Arial", 10, "bold"),
                               command=lambda: messagebox.showinfo("Ação", f"{text} clicado"))
    chat_log.window_create(tk.END, window=action_button)
    chat_log.insert(tk.END, "\n")


# Configuração principal da interface
root = tk.Tk()
root.title("Suporte ChatBot")
root.geometry("300x450")  # Tamanho reduzido
root.configure(bg="#f4f4f4")

# Cabeçalho
header_frame = tk.Frame(root, bg="#212121", height=40)
header_frame.pack(fill=tk.X)

header_icon = tk.Label(header_frame, text="💬", bg="#212121", fg="white", font=("Arial", 14))
header_icon.pack(side=tk.LEFT, padx=5)

header_title = tk.Label(header_frame, text="Suporte ChatBot", bg="#212121", fg="white", font=("Arial", 12, "bold"))
header_title.pack(side=tk.LEFT)

header_status = tk.Label(header_frame, text="Online", bg="#212121", fg="#00e676", font=("Arial", 10))
header_status.pack(side=tk.LEFT, padx=5)

# Fundo arredondado para o chat log
rounded_chat = create_rounded_rectangle(280, 250, 20, "#ffffff")
rounded_chat_label = tk.Label(root, image=rounded_chat, bg="#f4f4f4", bd=0)
rounded_chat_label.place(x=10, y=60)

# Chat log
chat_log = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, bg="#ffffff", fg="#333333", font=("Arial", 10), bd=0,
                   relief="flat", padx=5, pady=5)
chat_log.place(x=20, y=70, width=260, height=230)

# Estilo de mensagens
chat_log.tag_config("user", background="#fff9c4", foreground="#000000", font=("Arial", 10, "bold"), lmargin1=5,
                    lmargin2=5)
chat_log.tag_config("bot", background="#ffffff", foreground="#000000", font=("Arial", 10), lmargin1=5, lmargin2=5)

# Fundo arredondado para o campo de entrada
rounded_input = create_rounded_rectangle(260, 40, 20, "#ffffff")
rounded_input_label = tk.Label(root, image=rounded_input, bg="#f4f4f4", bd=0)
rounded_input_label.place(x=20, y=320)

# Entrada e botão de envio
input_frame = tk.Frame(root, bg="#f4f4f4")
input_frame.place(x=25, y=325, width=250, height=35)

user_input = tk.Entry(input_frame, font=("Arial", 10), bd=0, relief="flat", fg="#666666")
user_input.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

send_button = tk.Button(input_frame, text="Enviar", font=("Arial", 10, "bold"), bg="#1976d2", fg="white",
                        command=send_message)
send_button.pack(side=tk.RIGHT, padx=5)

# Mensagem de boas-vindas
chat_log.config(state=tk.NORMAL)
chat_log.insert(tk.END, "Suporte ChatBot:\nOlá, como posso ajudar você hoje?\n", "bot")
chat_log.config(state=tk.DISABLED)

# Rodapé
footer = tk.Label(root, text="Powered by ChatBot", bg="#f4f4f4", fg="#757575", font=("Arial", 8, "italic"))
footer.pack(side=tk.BOTTOM, pady=5)

# Inicia a interface
root.mainloop()
