package com.example.color_is;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class result_Activity extends AppCompatActivity {

    TextView text_result;
    String result_color_name;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_result);

        Intent intent = getIntent();
        int user_R_avg = intent.getIntExtra("user_R_avg",0);
        int user_G_avg = intent.getIntExtra("user_G_avg",0);
        int user_B_avg = intent.getIntExtra("user_B_avg",0);

        int[][] rgb_mat = { //47*5
                {255,255,255,1,27},
                {192,192,192,2,21},
                {211,211,211,3,23},
                {128,128,128,4,15},
                {79,79,79,5,10},
                {16,16,16,6,4},
                {139,16,16,7,24},
                {255,0,0,8,43},
                {255,0,160,9,6},
                {255,157,181,10,36},
                {232,163,153,11,28},
                {255,167,135,12,29},
                {255,93,81,13,36},
                {255,114,0,14,22},
                {255,75,0,15,29},
                {251,55,80,16,42},
                {255,40,0,17,35},
                {238,230,196,18,22},
                {255,225,107,19,15},
                {254,245,0,20,6},
                {252,177,0,21,10},
                {255,210,0,22,5},
                {205,239,0,23,6},
                {117,201,0,24,6},
                {0,196,171,25,6},
                {0,128,0,26,6},
                {128,128,0,27,1},
                {161,140,117,28,16},
                {0,100,0,29,6},
                {0,195,235,30,6},
                {1,130,246,31,9},
                {37,8,255,32,38},
                {0,30,102,33,10},
                {139,0,78,34,34},
                {176,119,207,35,33},
                {128,0,128,36,38},
                {144,0,32,37,29},
                {150,75,0,38,13},
                {208,67,0,39,23},
                {170,114,0,40,9},
                {228,151,0,41,11},
                {206,179,144,42,20},
                {241,194,118,43,20},
                {0,8,73,44,10},
                {174,198,220,45,21},
                {157,176,199,46,19},
                {46,52,73,47,9} };

        String[] color_name={
                "white", "silver", "light gray", "gray", "dark gray",
                "black", "deep red", "red", "pink", "light pink",
                "pale pink", "peach", "coral", "light orange", "neon orange",
                "orange pink", "orange", "ivory", "light yellow", "yellow",
                "mustard", "gold", "neon green", "light green", "mint",
                "green", "olive green", "khaki", "dark green", "sky blue",
                "neon blue", "blue", "navy", "wine", "lavender",
                "purple", "burgundy", "brown", "red brown", "khaki beige",
                "camel", "sand", "beige", "denim", "light cheong",
                "middle cheong", "black cheong"};
        int minimum=10000;

        for(int i=0; i<=46; i++){
            int d = Math.abs(user_R_avg - rgb_mat[i][0])
            + Math.abs(user_G_avg - rgb_mat[i][1]) + Math.abs(user_B_avg - rgb_mat[i][2]);
            if(d<=minimum) {
                minimum=d;
                result_color_name = color_name[rgb_mat[i][4]-1];
                i=47;
            }
        }//for end

        text_result = findViewById(R.id.text_result);
        text_result.setText(result_color_name);


    }
}