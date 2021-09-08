package com.example.color_is;

import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityOptionsCompat;
import androidx.core.content.PermissionChecker;

import android.Manifest;
import android.app.Activity;
import android.content.Intent;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.graphics.drawable.BitmapDrawable;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import com.gun0912.tedpermission.PermissionListener;
import com.gun0912.tedpermission.TedPermission;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class Upload_Activity extends AppCompatActivity {

    private static final String TAG = "color is";

    private Boolean isPermission = true;

    private static final int PICK_FROM_ALBUM = 1;
    //이 변수는 onActivityResult 에서 requestCode 로 반환되는 값입니다.
    private static final int PICK_FROM_CAMERA = 2;

    private File tempFile;//tempFile 에 받아온 이미지를 저장

    ImageView imageView;
    private Button btnResult;
    int R_avg=0;
    int G_avg=0;
    int B_avg=0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_upload);

        tedPermission();
        Button button = findViewById(R.id.btnGallery);
        imageView = findViewById(R.id.imageView);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // 권한 허용에 동의하지 않았을 경우 토스트를 띄웁니다.
                if(isPermission) {
                    mGetContet.launch("image/*");
                }
                else Toast.makeText(view.getContext(), getResources().getString(R.string.permission_2), Toast.LENGTH_LONG).show();
            }
        });


        //결과 액티비티로 인텐트
        btnResult = findViewById(R.id.btnResult);
        btnResult.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(Upload_Activity.this, result_Activity.class);
                intent.putExtra("user_R_avg",R_avg);
                intent.putExtra("user_G_avg",G_avg);
                intent.putExtra("user_B_avg",B_avg);
                startActivity(intent);
            }
        });


/*
        findViewById(R.id.btnCamera).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // 권한 허용에 동의하지 않았을 경우 토스트를 띄웁니다.
                if(isPermission) goToAlbum();
                else Toast.makeText(view.getContext(), getResources().getString(R.string.permission_2), Toast.LENGTH_LONG).show();
            }
        });

 */
    }//onCreate end

    /*
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode != Activity.RESULT_OK) {
            Toast.makeText(this, "취소 되었습니다.", Toast.LENGTH_SHORT).show();

            if (tempFile != null) {
                if (tempFile.exists()) {
                    if (tempFile.delete()) {
                        Log.e(TAG, tempFile.getAbsolutePath() + " 삭제 성공");
                        tempFile = null;
                    }
                }
            }

            return;
        }//if end
        /*
        if (requestCode == PICK_FROM_ALBUM) {

            Uri photoUri = data.getData();
            Cursor cursor = null;

            try {
                /
                 *  Uri 스키마를
                 *  content:/// 에서 file:/// 로  변경한다.
                 /
                String[] proj = {MediaStore.Images.Media.DATA};

                assert photoUri != null;
                cursor = getContentResolver().query(photoUri, proj, null, null, null);

                assert cursor != null;
                int column_index = cursor.getColumnIndexOrThrow(MediaStore.Images.Media.DATA);

                cursor.moveToFirst();

                tempFile = new File(cursor.getString(column_index));
            } finally {
                if (cursor != null) {
                    cursor.close();
                }//if end
            }//finally end
            //setImage();

        }//if end /
    }//onActivityResult end       */

    /*
    private void goToAlbum() {
        mGetContet.launch("image/*");
    }//앨범에서 이미지 가져오기

     */

    ActivityResultLauncher<String> mGetContet = registerForActivityResult(
            new ActivityResultContracts.GetContent(),
            new ActivityResultCallback<Uri>() {
                @Override
                public void onActivityResult(Uri result) {
                    if (result != null){
                        imageView.setImageURI(result);

                        //비트맵 변환
                        BitmapDrawable drawable = (BitmapDrawable) imageView.getDrawable();
                        Bitmap bitmap = drawable.getBitmap();

                        //rgb 평균값 추출하기
                        int[] A_ary = new int[9];
                        int[] R_ary = new int[9];
                        int[] G_ary = new int[9];
                        int[] B_ary = new int[9];

                        int rgb1 = bitmap.getPixel(92, 78); //원하는 좌표값 입력
                        A_ary[0] = Color.alpha(rgb1); //알파
                        R_ary[0] = Color.red(rgb1); //red값 추출
                        G_ary[0] = Color.green(rgb1); //green값 추출
                        B_ary[0] = Color.blue(rgb1); //blue값 추출

                        int rgb2 = bitmap.getPixel(92, 195); //원하는 좌표값 입력
                        A_ary[0] = Color.alpha(rgb2); //알파
                        R_ary[0] = Color.red(rgb2); //red값 추출
                        G_ary[0] = Color.green(rgb2); //green값 추출
                        B_ary[0] = Color.blue(rgb2); //blue값 추출

                        int rgb3 = bitmap.getPixel(92, 317); //원하는 좌표값 입력
                        A_ary[0] = Color.alpha(rgb3); //알파
                        R_ary[0] = Color.red(rgb3); //red값 추출
                        G_ary[0] = Color.green(rgb3); //green값 추출
                        B_ary[0] = Color.blue(rgb3); //blue값 추출

                        int rgb4 = bitmap.getPixel(247, 78); //원하는 좌표값 입력
                        A_ary[0] = Color.alpha(rgb4); //알파
                        R_ary[0] = Color.red(rgb4); //red값 추출
                        G_ary[0] = Color.green(rgb4); //green값 추출
                        B_ary[0] = Color.blue(rgb4); //blue값 추출

                        int rgb5 = bitmap.getPixel(247, 195); //원하는 좌표값 입력
                        A_ary[0] = Color.alpha(rgb5); //알파
                        R_ary[0] = Color.red(rgb5); //red값 추출
                        G_ary[0] = Color.green(rgb5); //green값 추출
                        B_ary[0] = Color.blue(rgb5); //blue값 추출

                        int rgb6 = bitmap.getPixel(247, 317); //원하는 좌표값 입력
                        A_ary[0] = Color.alpha(rgb6); //알파
                        R_ary[0] = Color.red(rgb6); //red값 추출
                        G_ary[0] = Color.green(rgb6); //green값 추출
                        B_ary[0] = Color.blue(rgb6); //blue값 추출

                        int rgb7 = bitmap.getPixel(408, 78); //원하는 좌표값 입력
                        A_ary[0] = Color.alpha(rgb7); //알파
                        R_ary[0] = Color.red(rgb7); //red값 추출
                        G_ary[0] = Color.green(rgb7); //green값 추출
                        B_ary[0] = Color.blue(rgb7); //blue값 추출

                        int rgb8 = bitmap.getPixel(408, 195); //원하는 좌표값 입력
                        A_ary[0] = Color.alpha(rgb8); //알파
                        R_ary[0] = Color.red(rgb8); //red값 추출
                        G_ary[0] = Color.green(rgb8); //green값 추출
                        B_ary[0] = Color.blue(rgb8); //blue값 추출

                        int rgb9 = bitmap.getPixel(408, 317); //원하는 좌표값 입력
                        A_ary[0] = Color.alpha(rgb9); //알파
                        R_ary[0] = Color.red(rgb9); //red값 추출
                        G_ary[0] = Color.green(rgb9); //green값 추출
                        B_ary[0] = Color.blue(rgb9); //blue값 추출

                        int r_sum = 0;
                        int g_sum = 0;
                        int b_sum = 0;

                        for (int i = 0; i < A_ary.length; i++) {
                            r_sum += R_ary[i];
                            g_sum += G_ary[i];
                            b_sum += B_ary[i];
                        }

                        R_avg=(int)r_sum/A_ary.length;
                        B_avg=(int)b_sum/A_ary.length;
                        G_avg=(int)g_sum/A_ary.length;

                    }

                }
            });


/*
    //카메라에서 이미지 가져오기
    private void takePhoto() {

        Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);

        try {
            tempFile = createImageFile();
        } catch (IOException e) {
            Toast.makeText(this, "이미지 처리 오류! 다시 시도해주세요.", Toast.LENGTH_SHORT).show();
            finish();
            e.printStackTrace();
        }
        if (tempFile != null) {

            Uri photoUri = Uri.fromFile(tempFile);
            intent.putExtra(MediaStore.EXTRA_OUTPUT, photoUri);
            startActivityForResult(intent, PICK_FROM_CAMERA);
        }
    }




     /  폴더 및 파일 만들기

    private File createImageFile() throws IOException {

        // 이미지 파일 이름 ( blackJin_{시간}_ )
        String timeStamp = new SimpleDateFormat("HHmmss").format(new Date());
        String imageFileName = "color is_" + timeStamp + "_";

        // 이미지가 저장될 폴더 이름 ( blackJin )
        File storageDir = new File(Environment.getExternalStorageDirectory() + "/color is/");
        if (!storageDir.exists()) storageDir.mkdirs();

        // 파일 생성
        File image = File.createTempFile(imageFileName, ".jpg", storageDir);
        Log.d(TAG, "createImageFile : " + image.getAbsolutePath());

        return image;
    }//createImageFile end
    */

/*
    private void setImage() {

        ImageView imageView = findViewById(R.id.imageView);

        BitmapFactory.Options options = new BitmapFactory.Options();
        Bitmap originalBm = BitmapFactory.decodeFile(tempFile.getAbsolutePath(), options);

        imageView.setImageBitmap(originalBm);

    }//갤러리에서 받아온 이미지 넣기
*/


    private void tedPermission() {

        PermissionListener permissionListener = new PermissionListener() {
            @Override
            public void onPermissionGranted() {
                // 권한 요청 성공
                isPermission = true;
            }

            @Override
            public void onPermissionDenied(ArrayList<String> deniedPermissions) {
                // 권한 요청 실패
                isPermission = false;
            }
        };

        TedPermission.with(this)
                .setPermissionListener(permissionListener)
                .setRationaleMessage(getResources().getString(R.string.permission_2))
                .setDeniedMessage(getResources().getString(R.string.permission_1))
                .setPermissions(Manifest.permission.WRITE_EXTERNAL_STORAGE, Manifest.permission.CAMERA)
                .check();

    }//권한 설정 tedPermission end


}



