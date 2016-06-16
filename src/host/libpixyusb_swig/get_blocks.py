from pixy import *

# Pixy Python SWIG get blocks example #

BLOCK_COUNT = 100

print("Pixy Python SWIG Example -- Get Blocks")

# Initialize Pixy Interpreter thread #
if pixy_init() < 0:
    print('failed to init')
    exit(1)

blocks = BlockArray(BLOCK_COUNT)
frame = 0

# Wait for blocks #
while 1:

    count = pixy_get_blocks(BLOCK_COUNT, blocks)

    if count > 0:
        # Blocks found #
        print('frame %3d:' % frame)
        frame += 1
        for index in range (0, count):
            print('[BLOCK_TYPE=%d SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' %
                  (blocks[index].type, blocks[index].signature, blocks[index].x, blocks[index].y, blocks[index].width,
                   blocks[index].height))
