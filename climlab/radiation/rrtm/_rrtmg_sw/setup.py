def configuration(parent_package='', top_path=None):
    import os
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils import fcompiler

    #  Set default compiler flags
    cppflags = ''
    f77flags = ''
    f90flags = ''
    # figure out which compiler we're going to use
    compiler = fcompiler.get_default_fcompiler()
    # set some fortran compiler-dependent flags (following CliMT code here)
    if compiler == 'gnu95':
        f77flags=['-ffixed-line-length-132', '-fdefault-real-8']
        f90flags=['-fdefault-real-8', '-fno-range-check', '-ffree-form']
        #f90flags=['-fdefault-real-8']
    elif compiler == 'intel' or compiler == 'intelem':
        f77flags='-132 -r8'
        f90flags='-132 -r8'
    print f90flags

    #here = os.path.abspath(os.path.dirname(__file__))
    #sourcelistfile = os.path.join(here, 'sources_in_order_of_compilation')
    #sourcelist = [line.rstrip() for line in open(sourcelistfile)]
    #sourcelist.append('_rrtmg_lw.pyf')
    sourcelist = ['_rrtmg_sw.pyf',
                  'rrtmg_sw_v4.0/gcm_model/modules/parkind.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/parrrsw.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_aer.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_cld.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_con.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg16.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg17.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg18.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg19.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg20.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg21.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg22.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg23.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg24.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg25.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg26.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg27.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg28.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_kg29.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_ncpar.f90',
                  'rrtmg_sw_k_g_climlab.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_ref.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_tbl.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_vsn.f90',
                  'rrtmg_sw_v4.0/gcm_model/modules/rrsw_wvn.f90',
                  'rrtmg_sw_v4.0/gcm_model/src/mcica_random_numbers.f90',
                  'rrtmg_sw_v4.0/gcm_model/src/mcica_subcol_gen_sw.f90',
                  'rrtmg_sw_v4.0/gcm_model/src/rrtmg_sw_vrtqdr.f90',
                  'rrtmg_sw_v4.0/gcm_model/src/rrtmg_sw_reftra.f90',
                  'rrtmg_sw_v4.0/gcm_model/src/rrtmg_sw_taumol.f90',
                  'rrtmg_sw_v4.0/gcm_model/src/rrtmg_sw_spcvmc.f90',
                  'rrtmg_sw_v4.0/gcm_model/src/rrtmg_sw_setcoef.f90',
                  'rrtmg_sw_v4.0/gcm_model/src/rrtmg_sw_init.f90',
                  'rrtmg_sw_v4.0/gcm_model/src/rrtmg_sw_cldprmc.f90',
                  'rrtmg_sw_v4.0/gcm_model/src/rrtmg_sw_rad.f90',
                  'Driver.f90']

    config = Configuration(package_name='_rrtmg_sw', parent_name=parent_package, top_path=top_path)
    config.add_extension(name='_rrtmg_sw',
                         sources=sourcelist,
                         extra_f90_compile_args=f90flags,
                         #f2py_options=['-c',],
                         )
    config.add_data_files(os.path.join('rrtmg_sw_v4.0', 'gcm_model', 'data', 'rrtmg_sw.nc'))

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(configuration=configuration)
