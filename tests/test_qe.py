import thotpy as th


folder = 'tests/samples/'


def test_read():
    ideal = {
        # relax.out
        'Energy'               : -1000.0,
        'Volume'               : 2.0,
        'Density'              : 1.0,
        'Alat'                 : 10,
        'BFGS converged'       : True,
        'BFGS failed'          : False,
        'Total force'          : 0.000001,
        'Total SCF correction' : 0.0,
        'Runtime'              : '48m 8.71s',
        'CELL_PARAMETERS_out'  : [
            '1.000000000   0.000000000   0.000000000',
            '0.000000000   1.000000000   0.000000000',
            '0.000000000   0.000000000   1.000000000'],
        'ATOMIC_POSITIONS_out' : [
            'I                1.0000000000        0.0000000000        0.0000000000',
            'C                0.0000000000        1.0000000000        0.0000000000',
            'N                0.0000000000        0.0000000000        1.0000000000'],
        # relax.in
        'K_POINTS'             : '2 2 2 0 0 0',
        'etot_conv_thr'        : 1.0e-12,
        'max_seconds'          : 1000,
        'pseudo_dir'           : "'./pseudos/'",
        'CELL_PARAMETERS'      : [
            '2.000000000000000   0.000000000000000   0.000000000000000',
            '0.000000000000000   2.000000000000000   0.000000000000000',
            '0.000000000000000   0.000000000000000   2.000000000000000'],
        'ATOMIC_SPECIES'       : [
            'I  126.90400   I.upf',
            'N   14.00650   N.upf',
            'C   12.01060   C.upf'],
        'ATOMIC_POSITIONS'     : [
            'I   5.000000000000000   0.000000000000000   0.000000000000000',
            'C   0.000000000000000   5.000000000000000   0.000000000000000',
            'N   0.000000000000000   0.000000000000000   5.000000000000000'],
    }
    result = th.qe.read_dir(folder=folder, in_str='relax.in', out_str='relax.out')
    for key in ideal:
        assert ideal[key] == result[key]


def test_scf_from_relax():
    ideal = {
        'calculation'      : "'scf'",
        'celldm(1)'        : 10.0,
        'ibrav'            : 0,
        'occupations'      : "'fixed'",
        'conv_thr'         : 2.0e-12,
        'CELL_PARAMETERS'  : [
            '1.000000000   0.000000000   0.000000000',
            '0.000000000   1.000000000   0.000000000',
            '0.000000000   0.000000000   1.000000000'],
        'ATOMIC_SPECIES'   : [
            'I  126.90400   I.upf',
            'N   14.00650   N.upf',
            'C   12.01060   C.upf'],
        'ATOMIC_POSITIONS' : [
            'I                1.0000000000        0.0000000000        0.0000000000',
            'C                0.0000000000        1.0000000000        0.0000000000',
            'N                0.0000000000        0.0000000000        1.0000000000'],
    }
    th.qe.scf_from_relax(folder=folder)
    result = th.qe.read_in(folder + 'scf.in')
    for key in ideal:
        assert ideal[key] == result[key]
    assert 'A' not in result.keys()
    try:
        th.file.remove(folder + 'scf.in')
    except:
        pass
