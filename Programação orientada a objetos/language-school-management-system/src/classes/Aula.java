package classes;

public class Aula {

    private String horario;
    private String data;
    private int numeroSala;
    private Turma turma;
    private Professor professor;
    private String disciplina;


    public Aula(String horario,String data, int numeroSala, Turma turma, Professor professor, String disciplina) {
        this.horario = horario;
        this.data = data;
        this.numeroSala = numeroSala;
        this.turma = turma;
        this.professor = professor;
        this.disciplina = disciplina;
    }
    
    public void setHorario(String horario) {
        this.horario = horario;
    }

    public String getHorario() {
        return this.horario;
    }

    public void setData(String data) {
        this.data = data;
    }

    public String getData() {
        return this.data;
    }

    public void setNumeroSala(int numeroSala) {
        this.numeroSala = numeroSala;
    }

    public int getNumeroSala() {
        return this.numeroSala;
    }

    public void setTurma(Turma turma) {
        this.turma = turma;
    }

    public Turma getTurma() {
        return this.turma;
    }

    public void setProfessor(Professor professor) {
        this.professor = professor;
    }

    public Professor getProfessor() {
        return this.professor;
    }

    public void setDisciplina(String disciplina) {
        this.disciplina = disciplina;
    }

    public String getDisciplina() {
        return this.disciplina;
    }

    public String toString() {
        return "Aula{" +
                "horario='" + this.horario + '\'' +
                ", numeroSala=" + this.numeroSala +
                ", turma=" + this.turma +
                ", professor=" + this.professor +
                '}';
    }
}
    


    
