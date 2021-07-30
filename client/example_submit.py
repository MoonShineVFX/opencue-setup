from opencue import api
from opencue.wrappers.show import Show
from outline import Outline, cuerun
from outline.modules.shell import Shell


# Define
SHOW_NAME = 'testShow'.lower()
ALLOCATION_NAME = 'local.general'

SHOT_NAME = 'testShot'
USER_NAME = 'robot'
FRAME_RANGE = '1-10'
JOB_NAME = 'testJob'

# Layers
first_layer = Shell('layer_first', command=['echo', '"Hi, im first. FRAME: #IFRAME#"'])
second_layer = Shell('layer_second', command=['echo', '"Yo, im second. FRAME: #IFRAME#"'])
second_layer.depend_on(first_layer)

# Outline
outline = Outline(JOB_NAME, frame_range=FRAME_RANGE, shot=SHOT_NAME, show=SHOW_NAME, user=USER_NAME)
outline.add_layer(first_layer)
outline.add_layer(second_layer)

# Create show if haven't
is_created = False
for show in api.getShows():
    if SHOW_NAME == show.data.name:
        is_created = True
        break
if not is_created:
    new_show: Show = api.createShow(SHOW_NAME)
    alloc = api.getAllocation(ALLOCATION_NAME)
    new_show.createSubscription(alloc, 1000, 1000)

# Submit
jobs = cuerun.launch(outline, use_pycuerun=False)
for job in jobs:
    job.setPriority(100)

print('Finish submitting')
