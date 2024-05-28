IN_VIDEO=$1
A1_EPS=$2
A2_EPS=$3
A_S=$4
A_E=$5
B1_EPS=$6
B2_EPS=$7
B_S=$8
B_E=$9
AB_OUT_VIDEO=${10}
BA_OUT_VIDEO=${11}

ffmpeg -y -i ${IN_VIDEO} -filter_complex \
"[0:v]trim=start=${A1_EPS}:end=${B1_EPS},setpts=PTS-STARTPTS[v0]" \
-map "[v0]" ${AB_OUT_VIDEO}


ffmpeg -y -i ${IN_VIDEO} -filter_complex \
"[0:v]trim=start=${B2_EPS}:end=${B1_EPS},setpts=PTS-STARTPTS[v0]; \
 [0:v]trim=start=${A2_EPS}:end=${B2_EPS},setpts=PTS-STARTPTS[v1]; \
 [0:v]trim=start=${A1_EPS}:end=${A2_EPS},setpts=PTS-STARTPTS[v2]; \
 [v0][v1][v2]concat=n=3:v=1:a=0[outv]" \
-map "[outv]" ${BA_OUT_VIDEO}