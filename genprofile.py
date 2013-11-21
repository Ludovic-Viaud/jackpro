import subprocess
import pstats

def main(script):
    #python -m cProfile [-o output_file] [-s sort_order] myscript.py
    subprocess.call('python -m cProfile -o profile %s.py' % script)
    flux = open('profile.txt', 'w')
    pstats.Stats('profile', stream=flux).sort_stats('time').print_stats()
    flux.close()


if __name__ == '__main__':
    main('countlib')