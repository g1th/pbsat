
#
# This file is the default set of rules to compile a Pebble project.
#
# Feel free to customize this to your needs.
#

from sh import jshint

top = '.'
out = 'build'

def options(ctx):
    ctx.load('pebble_sdk')

def configure(ctx):
    ctx.load('pebble_sdk')
    jshint.bake(['--config', 'pebble-jshintrc'])

def build(ctx):
    ctx.load('pebble_sdk')

    jshint("src/js/pebble-js-app.js")
    ctx.pbl_program(source=ctx.path.ant_glob('src/**/*.c'),
                    target='pebble-app.elf')

    ctx.pbl_bundle(elf='pebble-app.elf',
                   js=ctx.path.ant_glob('src/js/**/*.js'))
