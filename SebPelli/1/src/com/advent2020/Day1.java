package com.advent2020;

import java.io.File;

import java.io.FileNotFoundException;

import static java.lang.Integer.parseInt;

import java.util.ArrayList;

import java.util.Scanner;



public class Day1 {

    public static void read(ArrayList<Integer> numbers){

        String leggiDati;

        try {

            File file = new File("/Users/sebastianpelli/Desktop/Advent/Day1.2020");

            Scanner Lettore = new Scanner(file);

            while (Lettore.hasNextLine()) {

                leggiDati = Lettore.nextLine();

                numbers.add(parseInt(leggiDati));

            }

            Lettore.close();

        } catch (FileNotFoundException e) {

            System.out.println("Couldn't open the file");

            e.printStackTrace();

        }}



    public static void part1(ArrayList<Integer> numbers){

        long x=0;



        for (int i=0;i<numbers.size()-1;i++)

            if ( numbers.contains(2020 - numbers.get(i)))

                x = numbers.get(i) * (2020 - numbers.get(i));

        System.out.println("Part 1 =" + x);

    }

    public static void part2(ArrayList<Integer> numbers){

        long x=0;

        for (int i=0;i<numbers.size()-2;i++)

            for (int j=i+1;j<numbers.size()-1;j++)

                for (int k=j+1;k<numbers.size();k++)

                {

                    if (numbers.get(i) + numbers.get(j) + numbers.get(k) ==2020)

                    {

                        x = numbers.get(i) * numbers.get(j) * numbers.get(k);

                    }

                }

        System.out.println("Part 2 =" + x);

    }



    public static void main(String[] args){

        ArrayList<Integer> numbers = new ArrayList<>();

        Day1.read(numbers);

        Day1.part1(numbers);

        Day1.part2(numbers);

    }

};


