
from connectivity import Connectivity

def main():

    config_connectivity_conf = "/usr/lab/alum/0330717/Auror_workspace/cc.conf"

    software_catcher = MixCatcherFactory()
    auror_mix = software_catcher.getMixCatcher("Connectivity",4)
    auror_mix.catch(report_file, 4)


if __name__ == '__main__':
    main()
