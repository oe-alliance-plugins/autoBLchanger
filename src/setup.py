from setuptools import setup
import setup_translate

pkg = 'Extensions.autoBLchanger'
setup(name='enigma2-plugin-extensions-autoblchanger',
       version='3.0',
       description='automatic or manual BootlogoChanger for your E2-Box',
       package_dir={pkg: 'autoBLchanger'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'logos/*.jpg', 'logos/*.mvi']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
