package classes;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Boleto {
    private static int numeroBoletos = 0;
    private int idBoleto;
    private float valor;
    private Aluno aluno;
    private String vencimento;
    private boolean pago;

    public Boleto(float valor, Aluno aluno, String vencimento) {
        this.idBoleto = (++numeroBoletos*102);
        this.valor = valor;
        this.aluno = aluno;
        this.vencimento = vencimento;
        this.pago = false;
    }

    public void setIdBoleto(int idBoleto) {
        this.idBoleto = idBoleto;
    }
    
    public int getIdBoleto() {
        return this.idBoleto;
    }

    public void setValor(float valor) {
        this.valor = valor;
    }

    public float getValor() {
        return this.valor;
    }


    public void setAluno(Aluno aluno) {
        this.aluno = aluno;
    }

    public Aluno getBeneficiario() {
        return this.aluno;
    }

    public void setVencimento(String vencimento) {
        this.vencimento = vencimento;
    }

    public String getVencimento() {
        return this.vencimento;
    }

    public void setPago(boolean pago) {
        this.pago = pago;
    }

    public boolean getPago() {
        return this.pago;
    }

    public void gerarBoleto(String nomeArquivo, String numero, double valor, String beneficiario, String dataVencimento) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(nomeArquivo))) {
            // Escreve os dados do boleto no arquivo
            writer.write("Número do boleto: " + numero);
            writer.newLine();
            writer.write("Valor do boleto: " + valor);
            writer.newLine();
            writer.write("Beneficiário: " + beneficiario);
            writer.newLine();
            writer.write("Data de vencimento: " + dataVencimento);
        } catch (IOException e) {
            System.out.println("Erro ao gerar o boleto: " + e.getMessage());
        } catch (SecurityException e) {
            System.out.println("Erro de permissões: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Erro desconhecido: " + e.getMessage());
        }
    }

    public String toString() {
        return "Boleto{" +
                "idBoleto=" + this.idBoleto +
                ", valor=" + this.valor +
                ", aluno=" + this.aluno +
                ", vencimento='" + this.vencimento + '\'' +
                ", pago=" + this.pago +
                '}';
    }
}

