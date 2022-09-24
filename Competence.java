// package java;
import java.lang.Math;
import java.util.Arrays;
// package java;
public class Competence{
    public static void main(String[] args){
        double[] score;
        score = new double[5];
        int i;
        double sum = 0;
        double avg = 0;
        for(i=0;i<score.length;i++){
            score[i] = Math.random()*10;
        }
        Arrays.sort(score);
        for(i=1;i<score.length-1;i++){
            sum +=score[i]; 
        }
        avg = sum/(i-1);
        System.out.printf("%.2f",avg);
    }
}