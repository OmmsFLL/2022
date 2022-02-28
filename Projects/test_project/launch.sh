#!/bin/sh
# sshpass -p scp -rv * robot@ev3dev:test_project
sshpass -p maker rsync -av --delete "$PWD" robot@ev3dev:.
sshpass -p maker ssh robot@ev3dev "brickrun --directory \"/home/robot/${PWD##*/}\" \"/home/robot/${PWD##*/}/$1\""
