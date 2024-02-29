import tkinter as tk
from tkinter import ttk
import crud

class MainDB:
    def __init__(self, win):
        self.objBD = crud.AppBD()

        self.lblCodigo=tk.Label(win, text='Código do Produto')
        self.lblNome=tk.Label(win, text="Nome do produto")
        self.lblPreco=tk.Label(win, text="Preco")

        self.txtCodigo=tk.Entry(bd=3)
        self.txtNome=tk.Entry()
        self.txtPreco=tk.Entry()
        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)

        self.dadosColunas = ('Código', 'Nome','Preco')

        self.treeProdutos = ttk.Treeview(win, columns=self.dadosColunas, selectmode='browse')
        self.verscrlbar = ttk.Scrollbar(win, orient='vertical', command=self.treeProdutos.yview())
        self.verscrlbar.pack(side = 'right', fill = 'x')

        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)

        self.treeProdutos.heading('Código', text='Código')
        self.treeProdutos.heading('Nome', text='Nome')
        self.treeProdutos.heading('Preco', text='Preco')

        self.treeProdutos.column('Código',minwidth=0,width=100)
        self.treeProdutos.column('Nome',minwidth=0,width=100)
        self.treeProdutos.column('Preco',minwidth=0,width=100)

        self.treeProdutos.pack(padx=10, pady=10)

        self.treeProdutos.bind('<<TreeviewSelect>>', self.apresentarRegistrosSelecionados)


        self.lblCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)

        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)

        self.lblPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)

        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)

        self.treeProdutos.place(x=100, y=300)
        self.verscrlbar.place(x=805, y=300, height=225)
        self.carregarDadosIniciais()

    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeProdutos.selection():
            item = self.treeProdutos.item(selection)
            codigo,nome,preco = item['values'] [0:3]
            self.txtCodigo.insert(0,codigo)
            self.txtNome.insert(0, nome)
            self.txtPreco.insert(0, preco)

    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registros = self.objBD.selecionarDados()
            print('***************** dados disponíveis no BD *****************')
            for item in registros:
                codigo = item[0]
                nome = item[1]
                preco = item[2]
                print('Código = ', codigo)
                print('Nome = ', nome)
                print('Preço = ', preco, '\n')

                self.treeProdutos.insert('', 'end', iid = self.iid, values=(codigo, nome, preco))
                self.iid = self.iid + 1
                self.id = self.id + 1
            print('Dados da Base')
        except:
            print('Ainda não existem dados para carregar')

    def fLerCampos(self):
        try:
            print('************** dados disponíveis **************')
            codigo = int(self.txtCodigo.get())
            print('codigo', codigo)
            nome = self.txtNome.get()
            print('nome', nome)
            preco = float(self.txtPreco.get())
            print('preço', preco)
            print('Leitura dos Dados com sucesso')
        except:
            print('Não foi possível ler os dados')
        return codigo, nome, preco

    def dCadastrarProduto(self):
        try:
            print('******************* dados disponíveis ********************')
            codigo, nome, preco = self.fLerCampos()
            self.objBD.inserirDados(codigo, nome, preco)
            self.treeProdutos.insert('', 'end', iid=self.iid, values=(codigo, nome, preco))
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.fLimparTela()
            print('Produto Cadastrado com sucesso')
        except:
            print('Nao foi possivel fazer o cadastro')

    def fExcluirProduto(self):
        try:
            print('***************** dados disponíveis *********************')
            codigo, nome, preco = self.fLerCampos()
            self.objBD.excluirDados(codigo)

            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print('Produto Excluído com Sucesso')
        except:
            print('Não foi possível fazer a exclusão do produto')

    def fLimparTela(self):
        try:
            print('************** dados disponíveis ****************')
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print('Campos Limpos')
        except:
            print('Não foi possível limpar os campos')

window = tk.Tk()
main = MainDB(window)
window.title('Bem vindo a Aplicaçao de Banco de dados')
window.geometry("820x600+10+10")
window.mainloop()