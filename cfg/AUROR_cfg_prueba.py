import ConfigParser
import argparse
import sys

parser = argparse.ArgumentParser(description='configuration file')

parser.add_argument("level_of_test", help="ALTO/MEDIO/BAJO")
parser.add_argument("save_results", help="YES/NO")
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")


args = parser.parse_args()

if args.verbose:
    print("Verbosity turned on\n")


#DEFINE THE NAMES OF THE options
option_names = [
    'from_default',
    'level_of_test',
    'save_results',
    'from_section',
    'from_vars',
    'section_only',
    ]

#INITIALIZE THE PARSER WITH SOME DEFAULTS
config = ConfigParser.SafeConfigParser(
    defaults={'from_default'       : 'value from default passed to init',
              'level_of_test'      : 'value from default passed to init',
              'save_results'       : 'value from default passed to init',
              'from_section'       : 'value from default passed to init',
              'from_vars'          : 'value from default passed to init',
              'section_only'       : 'value from default passed to init',
            })

# Load the configuration file
config.read('with-defaults.ini')


def ConfigSectionMap(section) :
    dict1 = {}
    options = config.options(section)

    for option in options :
        try:
            dict1[option] = config.get(section,option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


config.set("DEFAULT", "level_of_test", args.level_of_test)
config.set("DEFAULT", "save_results", args.save_results)

for section_name in config.sections():
    print 'Section:', section_name
    print '  Options:', config.options(section_name)
    for name, value in config.items(section_name):
        print '  %s = %s' % (name, value)
    print


# Save the configuration file
config.write(sys.stdout)
