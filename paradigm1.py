#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on 四月 24, 2021, at 10:31
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'paradigm1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'Num': '', 'gender': '', 'age': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\张以昊\\大二下学期\\决策心理学\\延时折扣任务\\paradigm1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "introduction1"
introduction1Clock = core.Clock()
introduction1_1 = visual.ImageStim(
    win=win,
    name='introduction1_1', 
    image='document\\introduction1_1.png', mask=None,
    ori=0, pos=(0, 0), size=(1.76, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_1 = keyboard.Keyboard()

# Initialize components for Routine "device_use_time1"
device_use_time1Clock = core.Clock()
device_use_time1_1 = visual.ImageStim(
    win=win,
    name='device_use_time1_1', 
    image='document\\device_use_time.png', mask=None,
    ori=0, pos=(0, 0), size=(1.76, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
device_use_time = keyboard.Keyboard()

# Initialize components for Routine "introduction2"
introduction2Clock = core.Clock()
introduction2_1 = visual.ImageStim(
    win=win,
    name='introduction2_1', 
    image='document\\introduction2_1.png', mask=None,
    ori=0, pos=(0, 0), size=(1.76, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "time_percition"
time_percitionClock = core.Clock()
concentration = visual.TextStim(win=win, name='concentration',
    text='+',
    font=None,
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trumpet = visual.ImageStim(
    win=win,
    name='trumpet', 
    image='document\\laba.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='sound_1')
sound_1.setVolume(5)

# Initialize components for Routine "repeat_start"
repeat_startClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='请按下左键开始声音复制\n请按下右键结束声音复制',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
repeat_sound_start = keyboard.Keyboard()

# Initialize components for Routine "repeat_time"
repeat_timeClock = core.Clock()
text1 = visual.TextStim(win=win, name='text1',
    text='声音正在复制\n',
    font='hei',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
sound_2 = sound.Sound('A', secs=-1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
image_copy = visual.ImageStim(
    win=win,
    name='image_copy', 
    image='document\\\\laba.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_resp_sound_end = keyboard.Keyboard()

# Initialize components for Routine "introduction3"
introduction3Clock = core.Clock()

# Initialize components for Routine "delay_discount_task"
delay_discount_taskClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_1.keys = []
key_resp_1.rt = []
_key_resp_1_allKeys = []
# keep track of which components have finished
introduction1Components = [introduction1_1, key_resp_1]
for thisComponent in introduction1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction1"-------
while continueRoutine:
    # get current time
    t = introduction1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction1_1* updates
    if introduction1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction1_1.frameNStart = frameN  # exact frame index
        introduction1_1.tStart = t  # local t and not account for scr refresh
        introduction1_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction1_1, 'tStartRefresh')  # time at next scr refresh
        introduction1_1.setAutoDraw(True)
    
    # *key_resp_1* updates
    waitOnFlip = False
    if key_resp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_1.frameNStart = frameN  # exact frame index
        key_resp_1.tStart = t  # local t and not account for scr refresh
        key_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_1, 'tStartRefresh')  # time at next scr refresh
        key_resp_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_1.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_1_allKeys.extend(theseKeys)
        if len(_key_resp_1_allKeys):
            key_resp_1.keys = _key_resp_1_allKeys[-1].name  # just the last key pressed
            key_resp_1.rt = _key_resp_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction1"-------
for thisComponent in introduction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "device_use_time1"-------
continueRoutine = True
# update component parameters for each repeat
device_use_time.keys = []
device_use_time.rt = []
_device_use_time_allKeys = []
# keep track of which components have finished
device_use_time1Components = [device_use_time1_1, device_use_time]
for thisComponent in device_use_time1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
device_use_time1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "device_use_time1"-------
while continueRoutine:
    # get current time
    t = device_use_time1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=device_use_time1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *device_use_time1_1* updates
    if device_use_time1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        device_use_time1_1.frameNStart = frameN  # exact frame index
        device_use_time1_1.tStart = t  # local t and not account for scr refresh
        device_use_time1_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(device_use_time1_1, 'tStartRefresh')  # time at next scr refresh
        device_use_time1_1.setAutoDraw(True)
    
    # *device_use_time* updates
    waitOnFlip = False
    if device_use_time.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        device_use_time.frameNStart = frameN  # exact frame index
        device_use_time.tStart = t  # local t and not account for scr refresh
        device_use_time.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(device_use_time, 'tStartRefresh')  # time at next scr refresh
        device_use_time.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(device_use_time.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(device_use_time.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if device_use_time.status == STARTED and not waitOnFlip:
        theseKeys = device_use_time.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        _device_use_time_allKeys.extend(theseKeys)
        if len(_device_use_time_allKeys):
            device_use_time.keys = _device_use_time_allKeys[-1].name  # just the last key pressed
            device_use_time.rt = _device_use_time_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in device_use_time1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "device_use_time1"-------
for thisComponent in device_use_time1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if device_use_time.keys in ['', [], None]:  # No response was made
    device_use_time.keys = None
thisExp.addData('device_use_time.keys',device_use_time.keys)
if device_use_time.keys != None:  # we had a response
    thisExp.addData('device_use_time.rt', device_use_time.rt)
thisExp.nextEntry()
# the Routine "device_use_time1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
introduction2Components = [introduction2_1, key_resp_2]
for thisComponent in introduction2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction2"-------
while continueRoutine:
    # get current time
    t = introduction2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction2_1* updates
    if introduction2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction2_1.frameNStart = frameN  # exact frame index
        introduction2_1.tStart = t  # local t and not account for scr refresh
        introduction2_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction2_1, 'tStartRefresh')  # time at next scr refresh
        introduction2_1.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction2"-------
for thisComponent in introduction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop1 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('document\\material.xlsx'),
    seed=None, name='loop1')
thisExp.addLoop(loop1)  # add the loop to the experiment
thisLoop1 = loop1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
if thisLoop1 != None:
    for paramName in thisLoop1:
        exec('{} = thisLoop1[paramName]'.format(paramName))

for thisLoop1 in loop1:
    currentLoop = loop1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
    if thisLoop1 != None:
        for paramName in thisLoop1:
            exec('{} = thisLoop1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "time_percition"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_1.setSound('A', secs=emerge, hamming=False)
    sound_1.setVolume(5, log=False)
    # keep track of which components have finished
    time_percitionComponents = [concentration, trumpet, sound_1]
    for thisComponent in time_percitionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    time_percitionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "time_percition"-------
    while continueRoutine:
        # get current time
        t = time_percitionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=time_percitionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *concentration* updates
        if concentration.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            concentration.frameNStart = frameN  # exact frame index
            concentration.tStart = t  # local t and not account for scr refresh
            concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration, 'tStartRefresh')  # time at next scr refresh
            concentration.setAutoDraw(True)
        if concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                concentration.tStop = t  # not accounting for scr refresh
                concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration, 'tStopRefresh')  # time at next scr refresh
                concentration.setAutoDraw(False)
        
        # *trumpet* updates
        if trumpet.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            trumpet.frameNStart = frameN  # exact frame index
            trumpet.tStart = t  # local t and not account for scr refresh
            trumpet.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trumpet, 'tStartRefresh')  # time at next scr refresh
            trumpet.setAutoDraw(True)
        if trumpet.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trumpet.tStartRefresh + emerge-frameTolerance:
                # keep track of stop time/frame for later
                trumpet.tStop = t  # not accounting for scr refresh
                trumpet.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trumpet, 'tStopRefresh')  # time at next scr refresh
                trumpet.setAutoDraw(False)
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and t >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play()  # start the sound (it finishes automatically)
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + emerge-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in time_percitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "time_percition"-------
    for thisComponent in time_percitionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    # the Routine "time_percition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "repeat_start"-------
    continueRoutine = True
    # update component parameters for each repeat
    repeat_sound_start.keys = []
    repeat_sound_start.rt = []
    _repeat_sound_start_allKeys = []
    # keep track of which components have finished
    repeat_startComponents = [text, repeat_sound_start]
    for thisComponent in repeat_startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    repeat_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "repeat_start"-------
    while continueRoutine:
        # get current time
        t = repeat_startClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=repeat_startClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *repeat_sound_start* updates
        waitOnFlip = False
        if repeat_sound_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            repeat_sound_start.frameNStart = frameN  # exact frame index
            repeat_sound_start.tStart = t  # local t and not account for scr refresh
            repeat_sound_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(repeat_sound_start, 'tStartRefresh')  # time at next scr refresh
            repeat_sound_start.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(repeat_sound_start.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(repeat_sound_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if repeat_sound_start.status == STARTED and not waitOnFlip:
            theseKeys = repeat_sound_start.getKeys(keyList=['left'], waitRelease=False)
            _repeat_sound_start_allKeys.extend(theseKeys)
            if len(_repeat_sound_start_allKeys):
                repeat_sound_start.keys = _repeat_sound_start_allKeys[-1].name  # just the last key pressed
                repeat_sound_start.rt = _repeat_sound_start_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in repeat_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "repeat_start"-------
    for thisComponent in repeat_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "repeat_start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "repeat_time"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    sound_2.setSound('A', secs=20.0, hamming=True)
    sound_2.setVolume(1.0, log=False)
    key_resp_sound_end.keys = []
    key_resp_sound_end.rt = []
    _key_resp_sound_end_allKeys = []
    # keep track of which components have finished
    repeat_timeComponents = [text1, sound_2, image_copy, key_resp_sound_end]
    for thisComponent in repeat_timeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    repeat_timeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "repeat_time"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = repeat_timeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=repeat_timeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text1* updates
        if text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text1.frameNStart = frameN  # exact frame index
            text1.tStart = t  # local t and not account for scr refresh
            text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
            text1.setAutoDraw(True)
        if text1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text1.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text1.tStop = t  # not accounting for scr refresh
                text1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text1, 'tStopRefresh')  # time at next scr refresh
                text1.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                sound_2.stop()
        
        # *image_copy* updates
        if image_copy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_copy.frameNStart = frameN  # exact frame index
            image_copy.tStart = t  # local t and not account for scr refresh
            image_copy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_copy, 'tStartRefresh')  # time at next scr refresh
            image_copy.setAutoDraw(True)
        if image_copy.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_copy.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                image_copy.tStop = t  # not accounting for scr refresh
                image_copy.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_copy, 'tStopRefresh')  # time at next scr refresh
                image_copy.setAutoDraw(False)
        
        # *key_resp_sound_end* updates
        waitOnFlip = False
        if key_resp_sound_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_sound_end.frameNStart = frameN  # exact frame index
            key_resp_sound_end.tStart = t  # local t and not account for scr refresh
            key_resp_sound_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_sound_end, 'tStartRefresh')  # time at next scr refresh
            key_resp_sound_end.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_sound_end.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_sound_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_sound_end.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_sound_end.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_sound_end.tStop = t  # not accounting for scr refresh
                key_resp_sound_end.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_sound_end, 'tStopRefresh')  # time at next scr refresh
                key_resp_sound_end.status = FINISHED
        if key_resp_sound_end.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_sound_end.getKeys(keyList=['right'], waitRelease=False)
            _key_resp_sound_end_allKeys.extend(theseKeys)
            if len(_key_resp_sound_end_allKeys):
                key_resp_sound_end.keys = _key_resp_sound_end_allKeys[-1].name  # just the last key pressed
                key_resp_sound_end.rt = _key_resp_sound_end_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in repeat_timeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "repeat_time"-------
    for thisComponent in repeat_timeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_2.stop()  # ensure sound has stopped at end of routine
    # check responses
    if key_resp_sound_end.keys in ['', [], None]:  # No response was made
        key_resp_sound_end.keys = None
    loop1.addData('key_resp_sound_end.keys',key_resp_sound_end.keys)
    if key_resp_sound_end.keys != None:  # we had a response
        loop1.addData('key_resp_sound_end.rt', key_resp_sound_end.rt)
    thisExp.nextEntry()
    
# completed 2 repeats of 'loop1'


# ------Prepare to start Routine "introduction3"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
introduction3Components = []
for thisComponent in introduction3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction3"-------
while continueRoutine:
    # get current time
    t = introduction3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction3"-------
for thisComponent in introduction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "delay_discount_task"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
delay_discount_taskComponents = []
for thisComponent in delay_discount_taskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
delay_discount_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "delay_discount_task"-------
while continueRoutine:
    # get current time
    t = delay_discount_taskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=delay_discount_taskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in delay_discount_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "delay_discount_task"-------
for thisComponent in delay_discount_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "delay_discount_task" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
