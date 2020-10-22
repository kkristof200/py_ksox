from ksox import sox, ConcatSongElement

songs, total_len_s = sox.concat(
    [
        '/Users/kristofk/Downloads/Simulation_Chill_LofiHipHop.wav',
        '/Users/kristofk/Downloads/Untitled 1 - 7:30:20, 10.40 AM.wav',
        '/Users/kristofk/Downloads/Simulation_Chill_LofiHipHop.wav'
    ],
    'demo.wav',
    debug=True
    # 'tmp',
    # shape='h'
)

if songs:
    [s.jsonprint() for s in songs]
print(total_len_s)