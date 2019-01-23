from scipy.io import wavfile
import numpy as np 
import matplotlib.pyplot as plt
import glob

flute_notes = glob.glob('*.wav')

def get_fmphi(fs,note):

    
        threshold  = 0.5e8
        signal_fft = np.fft.fft(note)
        abs_fft = abs(signal_fft)
        output = np.zeros_like(abs_fft)

        for i, x in enumerate(abs_fft):
                if x > threshold :
                        output[i]  = signal_fft[i]
        return [fs, np.fft.ifft(output)]
    



def do_stuff(notes):
    for note in notes :
        # sampling frequency , actual note data 
        fs, data = wavfile.read(note)
        #create as many points as there are in data ( to make a plot)
        freq = np.linspace(0,fs,len(data))
        # gives fft with complex values in it
        
        fft_data  = np.fft.fft(data)
        # plot abs vs freq 
        abs_fft = np.abs(fft_data)
        #zooming down
        idx = int(0.09*len(data))
        plt.plot(freq[:idx],abs_fft[:idx])
        # setting labels
        plt.xlabel(note[-7:])
        plt.ylabel('fft of '+note[-7:])
        plt.show()


do_stuff(flute_notes)
