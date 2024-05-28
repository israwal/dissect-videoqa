import subprocess
import json
import os
import random
import argparse

random.seed(42)

def stitch_videos(vid_ann_path, charades_dir, out_dir):
    with open(vid_ann_path, 'r') as f:
        data = json.load(f)
    
    for i, (key, value) in enumerate(data.items()):
        print(value["vid_id"])
        q_key = key
        vid_id = value["vid_id"]
        [_, a_s, a_e] = value["info"][0]
        [_, b_s, b_e] = value["info"][1]
        [a1_eps, b1_eps, a2_eps, b2_eps] = list(value["ext"].values())
        vid_path = os.path.join(charades_dir, vid_id+".mp4")
        ab_path = os.path.join(out_dir, q_key + "_1" +".mp4")
        ba_path = os.path.join(out_dir, q_key + "_2" + ".mp4")

        cmd = " ".join(["bash", "./build_stitched_video.sh", vid_path, a1_eps, a2_eps, a_s, a_e, b1_eps, b2_eps, b_s, b_e, ab_path, ba_path])
        try:
            result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        except subprocess.CalledProcessError as e:
            # If the command failed, result.returncode will be the exit code of the process
            # and e.output will contain any error messages that were printed to stderr
            print(f"Error: {e}\n{e.output.decode()}")
    return


def main(args):
    charades_vid_dir = args.charades_vid_dir
    output_directory = args.output_directory 
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for split in ["train", "test"]:
        vid_ann_path = os.path.join('./json_files/', split+'_annotations.json')
        out_vids_save_path = os.path.join(output_directory, split)
        if not os.path.exists(out_vids_save_path):
            os.makedirs(out_vids_save_path)
        stitch_videos(vid_ann_path, charades_vid_dir, out_vids_save_path)

parser = argparse.ArgumentParser()
parser.add_argument('--charades_vid_dir', help='directory containing Charades videos')
parser.add_argument('--output_directory', help='directory for storing CLAVI videos')
args = parser.parse_args()

main(args)


    