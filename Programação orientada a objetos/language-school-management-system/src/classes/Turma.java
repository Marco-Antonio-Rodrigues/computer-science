package classes;

import java.util.ArrayList;

public class Turma {
    private static int numeroTurmas= 0;
    private int codigoTurma;
    private ArrayList<Aluno> alunos;
    private ArrayList<Aula> aulas;
    private int numeroAlunos;

    public Turma() {
        numeroTurmas++;
        this.codigoTurma = numeroTurmas*1001;
        this.alunos = new ArrayList<>();
        this.aulas = new ArrayList<>();
        this.numeroAlunos = 0;
    }

    public void setCodigoTurma(int codigoTurma) {
        this.codigoTurma = codigoTurma;
    }

    public int getCodigoTurma() {
        return this.codigoTurma;
    }

    public void setAlunos(ArrayList<Aluno> alunos) {
        this.alunos = alunos;
    }

    public ArrayList<Aluno> getAlunos() {
        return this.alunos;
    }

    public void setAulas(ArrayList<Aula> aulas) {
        this.aulas = aulas;
    }

    public ArrayList<Aula> getAulas() {
        return this.aulas;
    }

    public void setNumeroAlunos(int numeroAlunos) {
        this.numeroAlunos = numeroAlunos;
    }
    
    public int getNumeroAlunos() {
        return this.numeroAlunos;
    }

    public String toString() {
        return "Turma{" +
                "codigoTurma=" + this.codigoTurma +
                ", alunos=" + this.alunos +
                ", aulas=" + this.aulas +
                '}';
    }
}

    

