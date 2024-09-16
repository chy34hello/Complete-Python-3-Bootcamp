# Written by *** for COMP9021
#
# At stage 0, start with a toothpick centered at (0, 0).
# There is a free tip at the top, at coordinates (0, 2),
# and a free tip at the bottom, at coordinates (0, -2):
#
#         *
#         *
#         *
#         *
#         *
#
# At stage 1, perpendically place toothpicks on those tips.
# So there are now 3 toothpicks and 4 free tips,
# a top left one at coordinates (-2, 2),
# a top right one at coordinates (2, 2),
# a bottom left one at coordinates (-2, -2), and
# a bottom right one at coordinates (2, -2):
#
#     * * * * *
#         *
#         *
#         *
#     * * * * *
#
# At stage 2, perpendically place toothpicks on those tips.
# So there are now 7 toothpicks and 4 free tips,
# a top left one at coordinates (-2, 4),
# a top right one at coordinates (2, 4),
# a bottom left one at coordinates (-2, -4), and
# a bottom right one at coordinates (2, -4):
#
#
#     *       *
#     *       *
#     * * * * *
#     *   *   *
#     *   *   *
#     *   *   *
#     * * * * *
#     *       *
#     *       *
#
# Implements a function
# tooth_picks(stage, top_left_corner, bottom_right_corner)
# that displays, using black and white squares,
# that part of the plane that fits in a rectangle
# whose top left and bottom right corners are provided by the
# second and third arguments, respectively, at the stage of the
# construction provided by the first argument.
# You can assume that stage is any integer between 0 and 1000;
# top_left_corner and bottom_right_corner are arbitrary pairs
# of integers, but practically such that the output can fit
# on the screen.
#
# For a discussion about the construction, see
# https://www.youtube.com/watch?v=_UtCli1SgjI&t=66s
# The video also points to a website that you might find useful:
# https://oeis.org/A139250/a139250.anim.html

direction_vertical = 'VERTICAL'
direction_horizontal = 'HORIZONTAL'
paintBlack = '\N{black large square}'
paintWhite = '\N{white large square}'
toothpickHalfLen = 2
centerPosition = (0, 0)
freeTips_tracker = {centerPosition: direction_vertical}
historical_removed_Tips_tracker = dict()
howManyRoundsOfRemovedTipsThatIWantToTrack = 4


def tooth_picks(stage, top_left_corner, bottom_right_corner):
    board = initializeBoard(top_left_corner, bottom_right_corner)
    addMultipleRoundsOfToothspicksToBoard(stage, board)
    printBoard(board, top_left_corner, bottom_right_corner)


def initializeBoard(top_left_corner, bottom_right_corner):
    initialBoard = generateBoard(top_left_corner, bottom_right_corner)
    addingToothpick(initialBoard, centerPosition, direction_vertical)
    return initialBoard


def addMultipleRoundsOfToothspicksToBoard(stage, board):
    while stage:
        addToothpicksForCurrentRound(board, stage)
        # CleanUpUnusedHistoryTracker(stage)
        stage -= 1


def CleanUpUnusedHistoryTracker(stage):
    for key, value in dict(historical_removed_Tips_tracker).items():
        if value >= stage + howManyRoundsOfRemovedTipsThatIWantToTrack:
            del historical_removed_Tips_tracker[key]


def generateBoard(top_left_corner, bottom_right_corner):
    (a, b) = top_left_corner
    (c, d) = bottom_right_corner
    board_coordinates = dict()

    for y in range(b, d-1, -1):
        for x in range(a, c+1, 1):
            board_coordinates[(x, y)] = paintWhite
    return board_coordinates


def printBoard(board, top_left_corner, bottom_right_corner):
    if board:
        (a, b) = top_left_corner
        (c, d) = bottom_right_corner
        lenOfLine = c - a + 1
        lineContent = str()
        count = lenOfLine
        lineContent = constructLine(board, lenOfLine, lineContent, count)
        print(lineContent)


def constructLine(board, lenOfLine, lineContent, count):
    for coordinate in board:
        if count:
            lineContent += board[coordinate]
            count -= 1
        elif count == 0:
            print(lineContent)
            count = lenOfLine-1
            lineContent = board[coordinate]
    return lineContent


def addingToothpick(board, coordinate, direction):
    (x, y) = coordinate

    # if toothspickFits(board, direction, x, y):
    if toothpickShouldPaintVertically(direction):
            paintToothspickVertically(board, x, y)
    else:
            paintToothspickHorizontally(board, x, y)


def toothpickShouldPaintVertically(direction):
    return direction == direction_vertical


def paintToothspickHorizontally(board, x, y):
    for w in range(x-toothpickHalfLen, x+toothpickHalfLen+1, 1):
        if (w, y) in board:
            board[(w, y)] = paintBlack


def paintToothspickVertically(board, x, y):
    for h in range(y-toothpickHalfLen, y+toothpickHalfLen+1, 1):
        if (x, h) in board:
            board[(x, h)] = paintBlack


def toothspickFits(Matrix, direction, x, y):
    toothPickFitsTheboard = True
    if direction == direction_vertical:
        for h in range(y-toothpickHalfLen, y+toothpickHalfLen+1, 1):
            if (x, h) not in Matrix:
                toothPickFitsTheboard = False
    else:
        for w in range(x-toothpickHalfLen, x+toothpickHalfLen+1, 1):
            if (w, y) not in Matrix:
                toothPickFitsTheboard = False
    return toothPickFitsTheboard


def addToothpicksForCurrentRound(board, stage):

    for tip in dict(freeTips_tracker):
        (x, y) = tip
        if freeTipFacingUpOrDown(tip):
            processNewFreeTipCandiate(
                (x-toothpickHalfLen, y), direction_vertical, stage)
            processNewFreeTipCandiate(
                (x+toothpickHalfLen, y), direction_vertical, stage)

        else:
            processNewFreeTipCandiate(
                (x, y-toothpickHalfLen), direction_horizontal, stage)
            processNewFreeTipCandiate(
                (x, y+toothpickHalfLen), direction_horizontal, stage)
        removeFreeTipFromTrackerAndMarkTheTip(tip, stage)

    addToothspicksForFreeTips(board)


def freeTipFacingUpOrDown(tip):
    return freeTips_tracker[tip] == direction_horizontal


def processNewFreeTipCandiate(FreeTip_candiate, direction, stage):
    if FreeTip_candiate in freeTips_tracker:
        removeFreeTipFromTrackerAndMarkTheTip(FreeTip_candiate, stage)
    elif FreeTip_candiate in historical_removed_Tips_tracker:
        return
    else:
        freeTips_tracker[FreeTip_candiate] = direction


def removeFreeTipFromTrackerAndMarkTheTip(tip, stage):
    historical_removed_Tips_tracker[tip] = stage
    freeTips_tracker.pop(tip)


def addToothspicksForFreeTips(board):
    for tip in freeTips_tracker:
        addingToothpick(board, tip, freeTips_tracker[tip])

tooth_picks(879, (-67, 89), (-52, 60))