# -*- coding: utf-8 -*-

import glob, moviepy.editor

def generate_animation(fps=2):
    
    print 'generating movie\n'
    plots_list = glob.glob('../output/*')
    plots_list.sort()
    
    print plots_list

    if len(plots_list) > 0:

        clip = moviepy.editor.ImageSequenceClip(plots_list, fps)
            
        clip.write_videofile('../output/pref_attach_animation.mp4', fps)
    
    else:
    
        raise IOError('no image files found')
