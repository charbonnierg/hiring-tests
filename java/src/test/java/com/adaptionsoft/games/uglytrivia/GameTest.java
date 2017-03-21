package com.adaptionsoft.games.uglytrivia;

import com.googlecode.zohhak.api.TestWith;
import com.googlecode.zohhak.api.runners.ZohhakRunner;
import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.*;

@RunWith(ZohhakRunner.class)
public class GameTest {

    @TestWith({
            "0, Pop",
            "4, Pop",
            "8, Pop",
            "1, Science",
            "5, Science",
            "9, Science",
            "2, Sports",
            "6, Sports",
            "10, Sports",
            "3, Rock",
            "7, Rock",
            "11, Rock"
    })
    public void askQuestionProvidesTheCorrectCategory(int position, String category) throws Exception {
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        Game game = new Game();
        game.add("John");
        game.add("Maria");
        game.places[0] = position;

        game.askQuestion();

        Assert.assertEquals(category + " Question 0", lastLine(outputStream));

    }

    private String lastLine(ByteArrayOutputStream outputStream) {
        String[] allLines = outputStream.toString().split("\n");
        return allLines[allLines.length - 1];
    }
}