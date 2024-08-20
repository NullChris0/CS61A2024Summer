
import code
import functools
import inspect
import re
import signal
import sys
import math
import numbers
import builtins
import operator
't649kbi1B3_JgsYSH05198f8_d71'

def qP4369b_6(fn):
    'N2Z224D1a11L8e7L2_OA9_57'
    if (inspect.stack()[(((44 + -79) + (-17 + 75)) + ((42 + -78) + (96 + -82)))][int((((-0.44788246654616326 + 0.716890304652938) + (-0.27852189845872166 + 0.5157299132031907)) * 0))].f_locals[((('' + '__') + chr(110)) + ('' + ('ame' + '__')))] == (('_' + ('_' + 'm')) + (('' + 'ain_') + chr(95)))):
        args = sys.argv[(((203 + -78) + (-165 + 74)) + ((-45 + 36) + (-57 + 33))):]
        fn(*args)
    return fn
auI6 = str()

def BRQ90TPf0(fn):
    'SF_3z46_H_9mH4_g96W4p31_8kC6_'

    @functools.wraps(fn)
    def Q4972(*args, **wIN__68):
        global auI6
        l6ZV34 = [repr(e) for e in args]
        l6ZV34 += [((repr(FROeY_5) + chr(((91 + 65) + (-187 + 92)))) + repr(v)) for (FROeY_5, v) in wIN__68.items()]
        fKI_0((((('{0' + '}(') + chr(123)) + (str() + ('1' + '})'))).format(fn.__name__, (chr((97 + -53)) + chr((103 + -71))).join(l6ZV34)) + chr(((48 + 51) + (-4 + -37)))))
        auI6 += (str() + (('' + '  ') + (' ' + ' ')))
        try:
            result = fn(*args, **wIN__68)
            auI6 = auI6[:(- (((-20 + -92) + (20 + 7)) + ((-26 + 21) + (142 + -48))))]
        except Exception as e:
            fKI_0((fn.__name__ + (str() + ((' exited ' + 'v') + ('ia' + ' exception')))))
            auI6 = auI6[:(- (((-29 + -65) + (-26 + 71)) + ((90 + 57) + (-169 + 75))))]
            raise
        fKI_0(((('{0}(' + '{') + ('1}' + ') -')) + (('' + '> {') + ('2' + '}'))).format(fn.__name__, (chr((66 + -22)) + chr(32)).join(l6ZV34), result))
        return result
    return Q4972

def fKI_0(DlL_p):
    'd_6E5b83_z1vR0sGHZl_A80_'
    print((auI6 + re.sub(chr(((145 + -51) + (-183 + 99))), (chr(((-61 + 85) + (85 + -99))) + auI6), str(DlL_p))))

def J4W9():
    'v_0L30_95X8s7s0R22D6D12_X'
    O945S0M7 = inspect.stack()[(((-37 + -78) + (-21 + 98)) + ((44 + -32) + (127 + -100)))]
    fKI_0(((('Curre' + 'nt l') + ('ine:' + ' ')) + (('File "{' + 'f[1]}"') + (', line {f[2]}, ' + 'in {f[3]}'))).format(f=O945S0M7))

def z_18O89(msg=None):
    'x55_8_1r5t6_u643C_0M_k_K1'
    O945S0M7 = inspect.currentframe().f_back
    l7D_o2iLo = O945S0M7.f_globals.copy()
    l7D_o2iLo.update(O945S0M7.f_locals)

    def Nc_c61_(signum, O945S0M7):
        print()
        exit(int((((-0.2762015994170173 + 0.3487933428028409) + (-0.09628025372529658 + 0.4890896456749966)) * 0)))
    signal.signal(signal.SIGINT, Nc_c61_)
    if (not msg):
        (_, filename, m_2XuJE, _, _, _) = inspect.stack()[(((-41 + -62) + (11 + 19)) + ((231 + -82) + (1 + -76)))]
        msg = ((str() + ('I' + 'n')) + (('teractin' + 'g a') + ('t File "{0}", ' + 'line {1} \n'))).format(filename, m_2XuJE)
        msg += ((('   ' + ' Uni') + ('' + 'x:    <Control>')) + (('-D continues the ' + 'p') + ('ro' + 'gram; \n')))
        msg += ((('    Win' + 'dows: ') + ('<C' + 'on')) + (('trol' + '>-Z <En') + ('ter> cont' + 'inues the program; \n')))
        msg += (((' ' + ' ') + ('  exit' + '() o')) + (('r' + ' <Control>-C exits the pr') + ('ogra' + 'm')))
    code.interact(msg, None, l7D_o2iLo)
'z6E_DIP8mu_85qW4_L_0r'
if (sys.version_info[int(((-0.01566312335008546 + 0.17620047370842962) * int((0.935937346480176 * 0))))] < (((-35 + -65) + (-56 + 72)) + ((39 + 66) + (-53 + 35)))):

    def input(A3Ar0n_A):
        sys.stderr.write(A3Ar0n_A)
        sys.stderr.flush()
        m_2XuJE = sys.stdin.readline()
        if (not m_2XuJE):
            raise EOFError()
        return m_2XuJE.rstrip((str() + (str() + ('' + '\r\n'))))

class P4o99_69():
    'I9mN_1T___T466_49_K24_14_q'

    def __init__(self, Qls_9_):
        'rVmDE23_B35_4MG__da_P2_Es_49'
        self.index = int((((-1.2714013826769306 + 0.8750645959689087) + (0.40356426919984223 + 0.1957026761918066)) * 0))
        self.lines = []
        self.Qls_9_ = Qls_9_
        self.current_line = ()
        self.current()

    def b6_g2N7D3(self):
        'XO_Ef9x9_DI63zFU7_es4'
        current = self.current()
        self.index += (((-52 + 54) + (55 + -26)) + ((41 + -37) + (-73 + 39)))
        return current

    def current(self):
        'PxH0P2_254mGz3_60EDoI'
        while (not self.more_on_line()):
            try:
                self.index = int((((0.11383317145832972 + 0.51747117681729) + (-0.29887391025848997 + 0.4004719235621833)) * 0))
                self.current_line = next(self.Qls_9_)
                self.lines.append(self.current_line)
            except StopIteration:
                self.current_line = ()
                return None
        return self.current_line[self.index]

    def more_on_line(self):
        return (self.index < len(self.current_line))

    def end_of_line(self):
        return (self.current() is None)

    def __str__(self):
        'y55w5GD19M52Sc7_g1H0_475Kt8'
        WMN_cR = len(self.lines)
        msg = (((chr((129 + -6)) + (('' + '0:') + '>')) + str((math.floor(math.log10(WMN_cR)) + (((17 + -45) + (128 + -45)) + ((-36 + -97) + (39 + 40)))))) + (chr((174 + -49)) + (str() + ('' + ': '))))
        s = str()
        for i in range(max(int((((-0.4803306031808924 + 0.5169033256536263) + (0.2918555007387883 + 0.5008462742757752)) * 0)), (WMN_cR - ((int((0.4863714264271155 * 0)) + (-10 + -6)) + ((14 + 1) + (-28 + 33))))), (WMN_cR - (((-140 + 48) + (-51 + 100)) + ((62 + -51) + (127 + -94))))):
            s += ((msg.format((i + (((17 + 100) + (-86 + 65)) + ((-195 + 26) + (59 + 15))))) + chr(((78 + -37) + (11 + -20))).join(map(str, self.lines[i]))) + chr((-34 + 44)))
        s += msg.format(WMN_cR)
        s += chr(32).join(map(str, self.current_line[:self.index]))
        s += (chr((-42 + 74)) + (('>' + '>') + ' '))
        s += chr(32).join(map(str, self.current_line[self.index:]))
        return s.strip()
try:
    import readline as hM_i
except:
    pass

class u312__A_5():
    'Z_72M9KfpoJi3985LuU_5An34V_8T'

    def __init__(self, A3Ar0n_A):
        self.A3Ar0n_A = A3Ar0n_A

    def __iter__(self):
        while True:
            (yield input(self.A3Ar0n_A))
            self.A3Ar0n_A = (chr(((32 + -48) + (144 + -96))) * len(self.A3Ar0n_A))

class Lp50t_G_9():
    'w8VXd__gBMR_C0D29rE5C_49z0H7k'

    def __init__(self, lines, A3Ar0n_A, p_23o_o16=';'):
        self.lines = lines
        self.A3Ar0n_A = A3Ar0n_A
        self.p_23o_o16 = p_23o_o16

    def __iter__(self):
        while self.lines:
            m_2XuJE = self.lines.pop(int(((-0.08551423805643121 + 0.9950933238156499) * int((0.4149798387194421 * 0))))).strip(chr((-47 + 57)))
            if ((self.A3Ar0n_A is not None) and (m_2XuJE != str()) and (not m_2XuJE.lstrip().startswith(self.p_23o_o16))):
                print((self.A3Ar0n_A + m_2XuJE))
                self.A3Ar0n_A = (chr(((5 + -56) + (9 + 74))) * len(self.A3Ar0n_A))
            (yield m_2XuJE)
        raise EOFError

class Pair():
    'l4_O1B79_1O_qD57x__b5_q'

    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __repr__(self):
        return ((str() + ('P' + 'ai')) + (('r({' + '0}') + (',' + ' {1})'))).format(repr(self.first), repr(self.rest))

    def __str__(self):
        s = (chr(40) + repl_str(self.first))
        rest = self.rest
        while isinstance(rest, Pair):
            s += (chr(((16 + 82) + (-28 + -38))) + repl_str(rest.first))
            rest = rest.rest
        if (rest is not nil):
            s += (((' ' + '.') + chr((-14 + 46))) + repl_str(rest))
        return (s + chr(((-95 + 54) + (92 + -10))))

    def __len__(self):
        (WMN_cR, rest) = ((((50 + -15) + (-22 + 64)) + ((-124 + 70) + (57 + -79))), self.rest)
        while isinstance(rest, Pair):
            WMN_cR += (((-55 + 38) + (-86 + 94)) + ((62 + -41) + (-9 + -2)))
            rest = rest.rest
        if (rest is not nil):
            raise TypeError(((('le' + 'ngth a') + ('t' + 'tempted on improper lis')) + chr((73 + 43))))
        return WMN_cR

    def __eq__(self, p):
        if (not isinstance(p, Pair)):
            return False
        return ((self.first == p.first) and (self.rest == p.rest))

    def map(self, fn):
        'A5cS14G_7O2_74c2_4_1T_81'
        R___8y = fn(self.first)
        if ((self.rest is nil) or isinstance(self.rest, Pair)):
            return Pair(R___8y, self.rest.map(fn))
        else:
            raise TypeError(((('il' + 'l-formed list (cdr') + (' is ' + 'a')) + ((' promi' + 'se') + ')')))

    def s_bEA7fo8(self, fn):
        'M__ra1i1VAj4kC_we316X9dU9T1h0'
        R___8y = fn(self.first)
        if ((self.rest is nil) or isinstance(self.rest, Pair)):
            return scheme_append(R___8y, self.rest.s_bEA7fo8(fn))
        else:
            raise TypeError(((('ill-form' + 'ed list (cdr i') + ('s' + ' a')) + ('' + (' promise' + ')'))))

class nil():
    'JG1136lOb4Rk_05N86Y1__'

    def __repr__(self):
        return ('n' + ('' + ('i' + 'l')))

    def __str__(self):
        return (chr((103 + -63)) + chr((48 + -7)))

    def __len__(self):
        return int((((-0.8172808370783067 + 0.5179658648228682) + (-0.4995955287717925 + 0.854111237061424)) * int((0.21172275622939019 * 0))))

    def map(self, fn):
        return self

    def s_bEA7fo8(self, fn):
        return self
nil = nil()

def repl_str(val):
    'mTy_77v3_c_abUd_LwfPRTLz'
    if (val is True):
        return (chr(35) + chr(116))
    if (val is False):
        return (str() + (chr(35) + chr(102)))
    if (val is None):
        return ((('un' + 'de') + ('f' + 'i')) + ('' + ('' + 'ned')))
    if (isinstance(val, str) and val and (val[int((((-1.093790793739505 + 0.6615149431321795) + (-0.3836950014728262 + 0.8846650800873262)) * int((0.455090744359121 * 0))))] == chr((28 + 6)))):
        return ((chr((134 + -100)) + repr(val[(((133 + 39) + (-54 + -24)) + ((-44 + -93) + (86 + -42))):(- (((-14 + 70) + (14 + -36)) + ((-103 + 68) + (-83 + 85))))])[(((-8 + 31) + (68 + -6)) + ((-45 + -24) + (-8 + -7))):(- (((28 + -49) + (24 + -48)) + ((31 + -23) + (89 + -51))))]) + chr((-22 + 56)))
    return str(val)
'xaLti5_J60Nwg_0M__s7'
q684_84 = {chr(((188 + -93) + (-31 + -25))): ('' + ('q' + ('u' + 'ote'))), chr(((63 + -18) + (44 + 7))): ((chr(113) + ('ua' + 'siq')) + (('u' + 'ot') + 'e')), (str() + (str() + (',' + '@'))): ((('' + 'unqu') + ('' + 'ote-s')) + (('p' + 'l') + ('ic' + 'ing'))), chr(((10 + 21) + (-22 + 35))): (('' + ('un' + 'q')) + ('' + ('u' + 'ote')))}

def scheme_read(src):
    'j8__9P0bRH6X62hO8313__'
    if (src.current() is None):
        raise EOFError
    val = src.b6_g2N7D3()
    if (val == (str() + (str() + ('n' + 'il')))):
        return nil
    elif (val in set((chr((116 + -76)) + '['))):
        if (src.current() == chr(((153 + -95) + (-81 + 69)))):
            raise SyntaxError(((('. cann' + 'ot be') + (' the fir' + 'st')) + ((' ' + 'token in') + (' a lis' + 't'))))
        return LE_dg_72(src, val, {'(': chr((129 + -88)), chr((105 + -14)): ']'}[val])
    elif (val in q684_84):
        return Pair(q684_84[val], Pair(scheme_read(src), nil))
    elif (val not in s_L9hHL):
        return val
    else:
        raise SyntaxError(((('u' + 'nexpec') + ('te' + 'd toke')) + (chr(110) + (': ' + '{0}'))).format(val))

def LE_dg_72(src, C232B85T2='(', gPr_nW84L=')'):
    'z6M0T50MX_2MR417__zM___F2h82w'
    try:
        if (src.current() is None):
            raise SyntaxError(((str() + ('u' + 'n')) + (('expecte' + 'd end') + (' of fil' + 'e'))))
        elif (src.current() in set((chr((92 + -51)) + chr((95 + -2))))):
            if (src.current() != gPr_nW84L):
                raise SyntaxError(((('Expected {} t' + 'o match wi') + ('th {} bu' + 't ')) + (('got' + ' ') + ('{' + '}'))).format(gPr_nW84L, C232B85T2, src.current()))
            src.b6_g2N7D3()
            return nil
        elif (src.current() == chr(46)):
            src.b6_g2N7D3()
            expr = scheme_read(src)
            if (src.current() is None):
                raise SyntaxError(((('unexpe' + 'cte') + ('d' + ' en')) + (('d ' + 'of') + (' ' + 'file'))))
            if (src.b6_g2N7D3() != chr((102 + -61))):
                raise SyntaxError(((('expected' + ' on') + ('e ' + 'element af')) + ('t' + ('e' + 'r .'))))
            if builtins.DOTS_ARE_CONS:
                return expr
            else:
                return Pair(Pair(((str() + ('varia' + 'di')) + chr((12 + 87))), Pair(expr, nil)), nil)
        else:
            first = scheme_read(src)
            rest = LE_dg_72(src, C232B85T2, gPr_nW84L)
            return Pair(first, rest)
    except EOFError:
        raise SyntaxError(((('unexpected end of ' + 'f') + 'i') + ('' + ('' + 'le'))))

def r_k_R9(A3Ar0n_A='scm> '):
    'ZI17TXJ9q_X_hY35DCY4'
    return P4o99_69(AD_0Zpkm_(u312__A_5(A3Ar0n_A)))

def buffer_lines(lines, A3Ar0n_A='scm> ', t5wH09=False):
    'vKV1__Rw__eeS1o3_GJ0xP34'
    if t5wH09:
        x8839297 = lines
    else:
        x8839297 = Lp50t_G_9(lines, A3Ar0n_A)
    return P4o99_69(AD_0Zpkm_(x8839297))

def v7z76(m_2XuJE):
    'S56nK31_4131m7_Op0_9Y1515qP'
    e04U4_ = P4o99_69(AD_0Zpkm_([m_2XuJE]))
    result = scheme_read(e04U4_)
    if e04U4_.more_on_line():
        raise SyntaxError(((("read_line's argument can" + ' only be ') + ('a single elemen' + 't')) + ((', but re' + 'ce') + ('ived multi' + 'ple'))))
    return result

def l_X4A():
    'DPdfEg88b__X9_YkZ8o_'
    while True:
        try:
            src = r_k_R9(((chr(114) + ('' + 'ead')) + (str() + ('' + '> '))))
            while src.more_on_line():
                expression = scheme_read(src)
                if (expression == (str() + (chr(101) + ('x' + 'it')))):
                    print()
                    return
                print((chr((170 + -55)) + ('t' + ('' + 'r :'))), expression)
                print(((chr(114) + ('e' + 'p')) + (chr(114) + chr(58))), repr(expression))
        except (SyntaxError, ValueError) as err:
            print((type(err).__name__ + chr((58 + 0))), err)
        except (KeyboardInterrupt, EOFError):
            print()
            return

def qP4369b_6(*args):
    if (len(args) and ((('' + ('-' + '-')) + (chr(114) + ('ep' + 'l'))) in args)):
        l_X4A()

def scheme_procedurep(x):
    return isinstance(x, Procedure)

def scheme_listp(x):
    'hLKDtQ0__Dk699rSE38_3_bf'
    while (x is not nil):
        if (not isinstance(x, Pair)):
            return False
        x = x.rest
    return True

def scheme_booleanp(x):
    return ((x is True) or (x is False))

def scheme_numberp(x):
    return (isinstance(x, numbers.Real) and (not scheme_booleanp(x)))

def is_scheme_true(val):
    'rOU7l_3TXU8Bnw100RWH5rz1h'
    return (val is not False)

def is_scheme_false(val):
    'H36Rw85_B_7f06Lt_M8Oz__p2z_E4'
    return (val is False)

def scheme_stringp(x):
    return (isinstance(x, str) and x.startswith(chr((129 + -95))))

def scheme_symbolp(x):
    return (isinstance(x, str) and (not scheme_stringp(x)))

def scheme_nullp(x):
    return (type(x).__name__ == (('n' + chr(105)) + chr((173 + -65))))

def scheme_atomp(x):
    return (scheme_booleanp(x) or scheme_numberp(x) or scheme_symbolp(x) or scheme_nullp(x) or scheme_stringp(x))

def self_evaluating(expr):
    'Y103m_Ml_7n_Ld__L72Rq83_'
    return ((scheme_atomp(expr) and (not scheme_symbolp(expr))) or (expr is None))

def ev473(x):
    return (scheme_listp(x) and (scheme_length(x) == (((-62 + 51) + (-25 + -22)) + ((-19 + 3) + (117 + -41)))) and (x.first == ((chr(118) + ('a' + 'ria')) + (chr(100) + ('' + 'ic')))) and scheme_symbolp(x.rest.first))

def aLn9U(x):
    assert ev473(x)
    return x.rest.first

def validate_type(val, W9mJ___4F, FROeY_5, name):
    'PpH4pS5l_Q29e1_ram23o2'
    if (not W9mJ___4F(val)):
        msg = ((('argument {0} of {1} has wro' + 'n') + ('g ' + 'typ')) + (str() + ('e' + ' ({2})')))
        odZ6W_Ag_ = type(val).__name__
        if scheme_symbolp(val):
            odZ6W_Ag_ = ((('s' + 'ym') + ('' + 'bo')) + chr((120 + -12)))
        raise SchemeError(msg.format(FROeY_5, name, odZ6W_Ag_))
    return val

def validate_procedure(oprerator):
    'r__DoOu8NI666u8NV0R_84a_'
    if (not scheme_procedurep(oprerator)):
        raise SchemeError(((str() + ('{0} is not ca' + 'llable:')) + ((' {' + '1') + '}')).format(type(oprerator).__name__.lower(), repl_str(oprerator)))

def validate_form(expr, min, max=float('inf')):
    'G8u_8___nZWr_ZYi6E4vdkmVB_19f'
    if (not scheme_listp(expr)):
        raise SchemeError((((('ba' + 'dly ') + ('' + 'fo')) + (('r' + 'med e') + ('xpressi' + 'on: '))) + repl_str(expr)))
    ea9o = len(expr)
    if (ea9o < min):
        raise SchemeError(((('to' + 'o ') + ('few ope' + 'rands in')) + (('' + ' fo') + ('' + 'rm'))))
    elif (ea9o > max):
        raise SchemeError((('' + ('t' + 'oo')) + ((' ' + 'many operands') + (' in' + ' form'))))

def validate_formals(formals):
    'l_Mo9DsB_v7HZIs3_qU1t'
    WU_2UR_2m = set()

    def W28_8(symbol, y6KBm7_):
        if (ev473(symbol) and y6KBm7_):
            symbol = aLn9U(symbol)
        if (not scheme_symbolp(symbol)):
            raise SchemeError(((('non-' + 'symbol:') + chr(32)) + (('{' + '0') + '}')).format(symbol))
        if (symbol in WU_2UR_2m):
            raise SchemeError(((chr(100) + ('up' + 'l')) + (('icat' + 'e symbol: ') + ('' + '{0}'))).format(symbol))
        WU_2UR_2m.add(symbol)
    while isinstance(formals, Pair):
        W28_8(formals.first, (formals.rest is nil))
        formals = formals.rest
    if (formals != nil):
        import scheme as r3yp
        if builtins.DOTS_ARE_CONS:
            W28_8(formals, True)
        else:
            raise SchemeError(((('For' + 'ma') + ('l' + 's')) + ((' must' + ' b') + ('e a ' + 'list'))))
BUILTINS = []

def builtin(*name, need_env=False):
    'y0qWnkcO176fFZo4AC304F63JB8_'

    def add(py_func):
        for name in name:
            BUILTINS.append((name, py_func, name[int((((-0.2962714155377315 + 0.2832847350647507) + (0.6691944260351113 + 0.22273676684826116)) * int((0.2546959958295081 * 0))))], need_env))
        return py_func
    return add
builtin((('' + ('pr' + 'ocedur')) + ('' + ('e' + '?'))))(scheme_procedurep)
builtin((('l' + chr(105)) + (str() + ('st' + '?'))))(scheme_listp)
builtin((('' + ('' + 'at')) + ('' + ('om' + '?'))))(scheme_atomp)
builtin((str() + (str() + ('boolean' + '?'))))(scheme_booleanp)
builtin((str() + (('n' + 'um') + ('ber' + '?'))))(scheme_numberp)
builtin(((chr(115) + chr(121)) + (('' + 'mb') + ('o' + 'l?'))))(scheme_symbolp)
builtin(((('' + 'st') + chr(114)) + (str() + ('in' + 'g?'))))(scheme_stringp)
builtin((('' + ('n' + 'u')) + ('l' + ('' + 'l?'))))(scheme_nullp)

@builtin((('' + ('' + 'no')) + 't'))
def scheme_not(x):
    return (not is_scheme_true(x))

@builtin(((str() + ('eq' + 'u')) + ('' + ('' + 'al?'))))
def scheme_equalp(x, y):
    if (scheme_pairp(x) and scheme_pairp(y)):
        return (scheme_equalp(x.first, y.first) and scheme_equalp(x.rest, y.rest))
    elif (scheme_numberp(x) and scheme_numberp(y)):
        return (x == y)
    else:
        return ((type(x) == type(y)) and (x == y))

@builtin(((('' + 'eq') + chr(118)) + chr(63)))
def mf71898(x, y):
    return scheme_eqp(x, y)

@builtin((('' + ('' + 'eq')) + chr((115 + -52))))
def scheme_eqp(x, y):
    if (scheme_numberp(x) and scheme_numberp(y)):
        return (x == y)
    elif (scheme_symbolp(x) and scheme_symbolp(y)):
        return (x == y)
    else:
        return (x is y)

@builtin(((chr(112) + ('' + 'ai')) + ('' + ('' + 'r?'))))
def scheme_pairp(x):
    return (type(x).__name__ == (str() + (('P' + 'a') + ('i' + 'r'))))

@builtin((('' + ('sc' + 'heme-val')) + (('' + 'id-cdr') + chr(63))))
def scheme_valid_cdrp(x):
    return (scheme_pairp(x) or scheme_nullp(x) or scheme_promisep(x))

@builtin(((('p' + 'rom') + chr(105)) + ('' + ('se' + '?'))))
def scheme_promisep(x):
    return (type(x).__name__ == (('P' + ('' + 'romi')) + (str() + ('' + 'se'))))

@builtin(((chr(102) + ('' + 'or')) + ('' + ('c' + 'e'))))
def scheme_force(x):
    validate_type(x, scheme_promisep, int(((-0.23899288440633215 + 0.3347005170798233) * int((0.9291520612349091 * 0)))), (('' + ('' + 'pr')) + ('' + ('' + 'omise'))))
    return x.evaluate()

@builtin((str() + (('c' + 'dr-str') + ('e' + 'am'))))
def scheme_cdr_stream(x):
    validate_type(x, (lambda x: (scheme_pairp(x) and scheme_promisep(x.rest))), int(((0.7542537828289495 + 0.17120510704746816) * int((0.09329967235304648 * 0)))), ((('' + 'cd') + ('r-' + 'st')) + (chr(114) + ('' + 'eam'))))
    return scheme_force(x.rest)

@builtin(((str() + ('l' + 'en')) + (('' + 'gt') + chr(104))))
def scheme_length(x):
    validate_type(x, scheme_listp, int((((-0.6160488043519051 + 0.8049022477698698) + (-0.509984698032554 + 0.6327330411809512)) * int((0.5405285604828135 * 0)))), (chr(108) + (('' + 'en') + ('' + 'gth'))))
    if (x is nil):
        return int((((-0.4442885424380536 + 0.971254175736008) + (-0.4399375282990139 + 0.7567982200763766)) * int((0.5340670551767479 * 0))))
    return len(x)

@builtin(((chr(99) + ('o' + 'n')) + 's'))
def scheme_cons(x, y):
    return Pair(x, y)

@builtin((chr((35 + 64)) + (chr(97) + chr(114))))
def scheme_car(x):
    validate_type(x, scheme_pairp, 0, (chr((35 + 64)) + ('' + ('a' + 'r'))))
    return x.first

@builtin((str() + (('' + 'cd') + 'r')))
def scheme_cdr(x):
    validate_type(x, scheme_pairp, 0, (str() + (('c' + 'd') + chr(114))))
    return x.rest

@builtin(((('' + 'se') + ('t' + '-ca')) + (chr(114) + '!')))
def scheme_set_car(x, y):
    validate_type(x, scheme_pairp, int((((-0.3944658476161831 + 0.22349787122477294) + (0.3190299029334428 + 0.35226894871767633)) * int(((0.2900869034205734 + 0.03273777461526517) * int((0.010371225746755863 * 0)))))), ((chr(115) + chr(101)) + (('t' + '-') + ('car' + '!'))))
    x.first = y

@builtin((str() + (str() + ('' + 'set-cdr!'))))
def scheme_set_cdr(x, y):
    validate_type(x, scheme_pairp, int((((-1.3872262600103666 + 0.9445925012204973) + (0.732546422627524 + 0.10504686546487485)) * int((0.9576560032596697 * 0)))), (('' + ('s' + 'e')) + (('' + 't-cd') + ('r' + '!'))))
    if (not builtins.DOTS_ARE_CONS):
        validate_type(y, scheme_valid_cdrp, (((-10 + 94) + (-92 + 61)) + ((-46 + -71) + (156 + -91))), ((('' + 'se') + 't') + (('-cd' + 'r') + chr(33))))
    x.rest = y

@builtin(((chr(108) + 'i') + (str() + ('' + 'st'))))
def scheme_list(*vals):
    result = nil
    for e in reversed(vals):
        result = Pair(e, result)
    return result

@builtin(('' + (chr(97) + ('pp' + 'end'))))
def scheme_append(*vals):
    if (len(vals) == 0):
        return nil
    result = vals[(- (((-102 + 52) + (-95 + 82)) + ((-95 + 66) + (66 + 27))))]
    for i in range((len(vals) - (((103 + -99) + (-18 + 55)) + ((-147 + 81) + (79 + -52)))), (- (((-79 + 56) + (40 + 48)) + ((-58 + 43) + (-106 + 57)))), (- (((37 + -77) + (-31 + 77)) + ((46 + -16) + (-9 + -26))))):
        v = vals[i]
        if (v is not nil):
            validate_type(v, scheme_pairp, i, ((chr(97) + chr(112)) + ('' + ('pen' + 'd'))))
            r = p = Pair(v.first, result)
            v = v.rest
            while scheme_pairp(v):
                p.rest = Pair(v.first, result)
                p = p.rest
                v = v.rest
            result = r
    return result

@builtin(((('' + 'int') + ('e' + 'g')) + (chr(101) + ('' + 'r?'))))
def scheme_integerp(x):
    return (scheme_numberp(x) and (isinstance(x, numbers.Integral) or (int(x) == x)))

def _check_nums(*vals):
    'X4_43tySl0B442y8rK5q7'
    for (i, v) in enumerate(vals):
        if (not scheme_numberp(v)):
            msg = ((('op' + 'erand') + ('' + ' {0')) + (('} (' + '{1}) is not a n') + ('' + 'umber')))
            raise SchemeError(msg.format(i, v))

def _arith(fn, init, vals):
    'Jf8__n1_578_X925BNGw1d8KA7h_'
    _check_nums(*vals)
    s = init
    for val in vals:
        s = fn(s, val)
    s = _ensure_int(s)
    return s

def _ensure_int(x):
    if (int(x) == x):
        x = int(x)
    return x

@builtin(chr(((184 + -98) + (35 + -78))))
def scheme_add(*vals):
    return _arith(operator.add, int((((-0.4319491443648017 + 0.08587115129668499) + (0.21178237940472044 + 0.5186669179650696)) * int((0.8806128398973609 * 0)))), vals)

@builtin(chr(((116 + 3) + (1 + -75))))
def scheme_sub(val0, *vals):
    _check_nums(val0, *vals)
    if (len(vals) == int((0.9200403947156446 * 0))):
        return _ensure_int((- val0))
    return _arith(operator.sub, val0, vals)

@builtin(chr((-40 + 82)))
def scheme_mul(*vals):
    return _arith(operator.mul, (((-79 + -51) + (101 + -67)) + ((51 + 3) + (-1 + 44))), vals)

@builtin(chr(((33 + -39) + (-40 + 93))))
def scheme_div(val0, *vals):
    _check_nums(val0, *vals)
    try:
        if (len(vals) == int(((-0.2661648088651317 + 0.8194046451895014) * int((0.12880724128515342 * 0))))):
            return _ensure_int(operator.truediv((((69 + -60) + (127 + -95)) + (int((0.5603120867137885 * 0)) + (-24 + -16))), val0))
        return _arith(operator.truediv, val0, vals)
    except ZeroDivisionError as err:
        raise SchemeError(err)

@builtin(((chr(101) + ('' + 'xp')) + chr((195 + -79))))
def scheme_expt(val0, val1):
    _check_nums(val0, val1)
    return pow(val0, val1)

@builtin((str() + ('' + ('' + 'abs'))))
def scheme_abs(val0):
    return abs(val0)

@builtin(((chr(113) + ('' + 'uotien')) + chr((48 + 68))))
def scheme_quo(val0, val1):
    _check_nums(val0, val1)
    try:
        return ((- ((- val0) // val1)) if ((val0 < int(((-0.19380317524355872 + 0.4424114877156706) * 0))) ^ (val1 < int((((-0.6025923399133859 + 0.23890579285205638) + (0.11220400274932696 + 0.658688293012319)) * 0)))) else (val0 // val1))
    except ZeroDivisionError as err:
        raise SchemeError(err)

@builtin(('m' + (('o' + 'd') + ('' + 'ulo'))))
def scheme_modulo(val0, val1):
    _check_nums(val0, val1)
    try:
        return (val0 % val1)
    except ZeroDivisionError as err:
        raise SchemeError(err)

@builtin((chr((205 + -91)) + (('ema' + 'i') + ('nde' + 'r'))))
def scheme_remainder(val0, val1):
    _check_nums(val0, val1)
    try:
        result = (val0 % val1)
    except ZeroDivisionError as err:
        raise SchemeError(err)
    while (((result < int((((-0.4052028380405043 + 0.8540492413963782) + (0.2591543056801312 + 0.16591594510338725)) * int((0.09352960351669104 * 0))))) and (val0 > int((((-0.9873780252990658 + 0.7802365089176485) + (0.610297593847333 + 0.33654809238392513)) * int(((0.590433993347739 + 0.29038356863558934) * int((0.8558730456578716 * 0)))))))) or ((result > 0) and (val0 < int((((0.2893188264625881 + 0.16423841032889452) + (-0.5675120761365503 + 0.8437599731633175)) * int(((0.16846292595120782 + 0.7060831786282621) * 0))))))):
        result -= val1
    return result

def number_fn(module, name, fallback=None):
    'e6NW5_pAuy020mKvtYQ7'
    py_fn = (getattr(module, name) if (fallback is None) else getattr(module, name, fallback))

    def scheme_fn(*vals):
        _check_nums(*vals)
        return py_fn(*vals)
    return scheme_fn
for _name in [((str() + ('' + 'ac')) + ('o' + 's')), ((str() + ('ac' + 'o')) + ('' + ('s' + 'h'))), (('a' + ('s' + 'i')) + 'n'), ((('a' + 's') + chr(105)) + (str() + ('' + 'nh'))), (chr(97) + (str() + ('t' + 'an'))), ((('a' + 't') + ('' + 'an')) + chr((71 + -21))), (str() + (('' + 'at') + ('' + 'anh'))), ('' + ('c' + ('e' + 'il'))), (('c' + chr(111)) + (('py' + 'sig') + chr(110))), (str() + (('c' + 'o') + chr(115))), (('c' + 'o') + ('' + ('' + 'sh'))), ('' + (('' + 'degr') + ('e' + 'es'))), ((str() + ('f' + 'lo')) + (chr(111) + chr(114))), ('' + (('l' + 'o') + chr(103))), ((('l' + 'o') + ('g' + '1')) + '0'), (chr((131 + -23)) + (str() + ('og1' + 'p'))), ((('ra' + 'd') + chr(105)) + (('a' + 'n') + 's')), (chr(115) + (str() + ('' + 'in'))), (str() + ('' + ('s' + 'inh'))), (('' + ('' + 'sq')) + (str() + ('r' + 't'))), ((str() + ('t' + 'a')) + 'n'), ((str() + ('t' + 'a')) + (chr(110) + chr(104))), ('' + (chr(116) + ('r' + 'unc')))]:
    builtin(_name)(number_fn(math, _name))
builtin((('' + ('' + 'lo')) + (chr(103) + '2')))(number_fn(math, ((('l' + 'o') + chr(103)) + chr((3 + 47))), (lambda x: math.log(x, (((11 + -75) + (-74 + 45)) + ((-20 + 73) + (82 + -40)))))))

def _numcomp(op, x, y):
    _check_nums(x, y)
    return op(x, y)

@builtin(chr(((155 + -54) + (3 + -43))))
def scheme_eq(x, y):
    return _numcomp(operator.eq, x, y)

@builtin(chr((17 + 43)))
def scheme_lt(x, y):
    return _numcomp(operator.lt, x, y)

@builtin(chr(62))
def scheme_gt(x, y):
    return _numcomp(operator.gt, x, y)

@builtin((str() + (str() + ('' + '<='))))
def U5N__B_RR(x, y):
    return _numcomp(operator.le, x, y)

@builtin((str() + (str() + ('>' + '='))))
def M_8fT_l7(x, y):
    return _numcomp(operator.ge, x, y)

@builtin((str() + (('' + 'ev') + ('' + 'en?'))))
def rUq0_hw(x):
    _check_nums(x)
    return ((x % (((93 + -75) + (-24 + -18)) + ((127 + -21) + (2 + -82)))) == int((((-0.47875959875758645 + 0.8885069766945636) + (-0.3497832643714991 + 0.7928410206380043)) * int((0.19307764945230854 * 0)))))

@builtin((chr((96 + 15)) + (str() + ('' + 'dd?'))))
def O5z_(x):
    _check_nums(x)
    return ((x % (((84 + -57) + (136 + -97)) + ((-10 + 1) + (-43 + -12)))) == (((8 + -88) + (-11 + 43)) + ((-71 + 59) + (160 + -99))))

@builtin((chr((134 + -12)) + ('e' + ('' + 'ro?'))))
def hq69__wI8(x):
    _check_nums(x)
    return (x == int(((0.5979265954588404 + 0.3168523471722301) * int((0.18649986525890128 * 0)))))

@builtin(((str() + ('di' + 's')) + ('p' + ('' + 'lay'))))
def V3lqE9(*vals):
    vals = [repl_str((val[(((-72 + -2) + (16 + 10)) + ((-2 + -46) + (1 + 96))):(- (((82 + -64) + (23 + -12)) + ((-129 + 8) + (4 + 89))))] if scheme_stringp(val) else val)) for val in vals]
    print(*vals, end=str())

@builtin(((('' + 'pr') + ('' + 'in')) + chr((132 + -16))))
def H_8_WT_(*vals):
    vals = [repl_str(val) for val in vals]
    print(*vals)

@builtin(((('' + 'di') + chr(115)) + (('' + 'pl') + ('a' + 'yln'))))
def iFoiu_9P(*vals):
    V3lqE9(*vals)
    wt45LpX()

@builtin((str() + (str() + ('n' + 'ewline'))))
def wt45LpX():
    print()
    sys.stdout.flush()

@builtin(((chr(101) + ('r' + 'ro')) + 'r'))
def u7su_340(msg=None):
    msg = (str() if (msg is None) else repl_str(msg))
    raise SchemeError(msg)

@builtin((('e' + chr(120)) + ('' + ('i' + 't'))))
def scheme_exit():
    raise EOFError

@builtin((str() + (('' + 'ma') + 'p')), need_env=True)
def scheme_map(fn, s, env):
    validate_type(fn, scheme_procedurep, 0, (chr(109) + (str() + ('' + 'ap'))))
    validate_type(s, scheme_listp, (((-47 + 44) + (-7 + -82)) + ((-84 + 89) + (-7 + 95))), (('' + ('' + 'ma')) + chr(112)))
    return s.map((lambda x: complete_apply(fn, Pair(x, nil), env)))

@builtin((chr(102) + ('' + ('il' + 'ter'))), need_env=True)
def scheme_filter(fn, s, env):
    validate_type(fn, scheme_procedurep, 0, ((('' + 'fil') + ('t' + 'e')) + chr((33 + 81))))
    validate_type(s, scheme_listp, (((-129 + 88) + (11 + -9)) + ((1 + 49) + (66 + -76))), (('' + ('f' + 'i')) + (('' + 'lte') + chr(114))))
    (head, current) = (nil, nil)
    while (s is not nil):
        (item, s) = (s.first, s.rest)
        if complete_apply(fn, Pair(item, nil), env):
            if (head is nil):
                head = Pair(item, nil)
                current = head
            else:
                current.rest = Pair(item, nil)
                current = current.rest
    return head

@builtin(((chr(114) + 'e') + ('' + ('du' + 'ce'))), need_env=True)
def scheme_reduce(fn, s, env):
    validate_type(fn, scheme_procedurep, int((((-0.11744508626393368 + 0.4532245637138371) + (0.23820161324489286 + 0.17618388445770028)) * int(((0.416068414726376 + 0.5406876425624073) * 0)))), ((('re' + 'd') + chr(117)) + (str() + ('' + 'ce'))))
    validate_type(s, (lambda x: (x is not nil)), (((-44 + 61) + (-13 + 42)) + ((-96 + 80) + (-122 + 93))), ((chr(114) + 'e') + (('' + 'du') + ('c' + 'e'))))
    validate_type(s, scheme_listp, (((-41 + -43) + (-59 + 51)) + ((131 + -41) + (19 + -16))), (('r' + ('' + 'educ')) + 'e'))
    (value, s) = (s.first, s.rest)
    while (s is not nil):
        value = complete_apply(fn, scheme_list(value, s.first), env)
        s = s.rest
    return value

@builtin((('' + ('l' + 'o')) + ('a' + chr(100))), need_env=True)
def scheme_load(*args):
    'M__6ix945__7Wx_861w_Z'
    if (not ((((-95 + 72) + (-1 + 74)) + ((-158 + 98) + (-79 + 91))) <= len(args) <= (((-83 + 21) + (24 + -15)) + ((38 + -15) + (-21 + 54))))):
        expressions = args[:(- (((-127 + 35) + (81 + -9)) + ((-31 + 14) + (-25 + 63))))]
        raise SchemeError(((('"loa' + 'd') + ('" given' + ' inc')) + (('orrect' + ' number ') + ('of arguments: {' + '0}'))).format(len(expressions)))
    sym = args[int((0.32897422328420645 * 0))]
    quiet = (args[(((102 + -33) + (-50 + -27)) + ((71 + -83) + (43 + -22)))] if (len(args) > (((8 + -88) + (169 + -91)) + ((-175 + 82) + (127 + -30)))) else True)
    env = args[(- (((87 + 30) + (-34 + -5)) + ((-94 + -60) + (171 + -94))))]
    if scheme_stringp(sym):
        sym = eval(sym)
    validate_type(sym, scheme_symbolp, int((((-1.0195079104394935 + 0.8148651999118958) + (0.3850144114291896 + 0.0841671703275938)) * int(((-0.08411163126454169 + 0.3060540094421137) * int((0.6089955042625718 * 0)))))), (('' + ('lo' + 'a')) + chr((186 + -86))))
    with scheme_open(sym) as infile:
        lines = infile.readlines()
    args = ((lines, None) if quiet else (lines,))

    def next_line():
        return buffer_lines(*args)
    pe_73 = env.stack[:]
    env.stack[:] = []
    read_eval_print_loop(next_line, env, quiet=quiet, report_errors=True)
    env.stack[:] = pe_73

@builtin(('' + (('load' + '-al') + chr(108))), need_env=True)
def scheme_load_all(directory, env):
    'KLE_yj4u_2h3L_9_74wD_4_o_9'
    assert scheme_stringp(directory)
    directory = directory[(((21 + -84) + (-15 + -18)) + ((108 + -94) + (101 + -18))):(- (((36 + 75) + (-99 + 31)) + ((8 + -34) + (26 + -42))))]
    import os as os
    for x in sorted(os.listdir('.')):
        if (not x.endswith(('.' + (('s' + 'c') + chr(109))))):
            continue
        scheme_load(x, env)

def scheme_open(filename):
    'wF__8x7D_8_ph_2o3t60_9'
    try:
        return open(filename)
    except IOError as exc:
        if filename.endswith((('' + ('' + '.s')) + (chr(99) + chr(109)))):
            raise SchemeError(str(exc))
    try:
        return open((filename + (chr(46) + (str() + ('s' + 'cm')))))
    except IOError as exc:
        raise SchemeError(str(exc))
zK_77D05_ = t_9H5Y_ = None

def RG95W():
    import turtle as SQY8_8_7
    SQY8_8_7.title(((('Sche' + 'me Turtl') + 'e') + chr(115)))

def h_4c_():
    try:
        from abstract_turtle import turtle as zK_77D05_
    except ImportError:
        raise SchemeError(((('Could not find abstract_turtle. This shoul' + 'd never happe') + ('n in student-facing situat' + 'ions. If you ar')) + (('e a student' + ', please file a bug') + (' on Pi' + 'azza.'))))
    return zK_77D05_

def n03L271K():
    try:
        import tkinter as _
    except:
        raise SchemeError(chr(((28 + 55) + (-36 + -37))).join([((('C' + 'o') + ('uld no' + 't')) + ((' import tkinter, so the' + ' tk-turtle will not') + (' w' + 'ork.'))), ((('Either install python wi' + 'th tkinter s') + ('upport o' + 'r run in')) + ((' pi' + 'llow-turtle') + (' ' + 'mode')))]))
    from abstract_turtle import TkCanvas as h825J958A
    return h825J958A((((1075 + 32) + (-25 + -35)) + ((-110 + 76) + (42 + -55))), (((1008 + -59) + (-32 + 21)) + ((14 + -47) + (135 + -40))), init_hook=RG95W)

def j1_2_P70_():
    try:
        import PIL as _
        import numpy as _
    except:
        raise SchemeError(chr((41 + -31)).join([((('C' + 'ould no') + ('t import abstract_turt' + 'le[pillow')) + (('_' + 'can') + ("vas]'s " + 'dependencies.'))), ((('' + 'To') + ('' + ' install these ')) + (('pa' + 'c') + ('kages, ru' + 'n'))), ((('    python3 -m p' + 'ip instal') + ('' + "l 'abstract_t")) + (('urt' + 'le[pillow_can') + ('va' + "s]'"))), ((('You can also run i' + 'n tk-turtle mo') + ('de by removing ' + 'the fl')) + (('' + 'ag `--pil') + ('low-tu' + 'rtle`')))]))
    from abstract_turtle import PillowCanvas as xM97T3A
    return xM97T3A((((1109 + -8) + (-39 + -55)) + ((37 + -76) + (-51 + 83))), (((1059 + -56) + (8 + -11)) + 0))

def qMV_():
    global zK_77D05_, t_9H5Y_
    if (zK_77D05_ is not None):
        return
    N92S61 = h_4c_()
    if builtins.TK_TURTLE:
        try:
            I4IO57K2 = n03L271K()
        except SchemeError as e:
            print(e, file=sys.stderr)
            print(((('At' + 'tempting pillow c') + ('anvas ' + 'mo')) + (chr(100) + 'e')), file=sys.stderr)
            I4IO57K2 = j1_2_P70_()
    else:
        I4IO57K2 = j1_2_P70_()
    (zK_77D05_, t_9H5Y_) = (N92S61, I4IO57K2)
    zK_77D05_.set_canvas(t_9H5Y_)
    zK_77D05_.mode((chr((80 + 28)) + (str() + ('' + 'ogo'))))

@builtin(((('fo' + 'r') + 'w') + ('a' + ('r' + 'd'))), (chr((126 + -24)) + 'd'))
def Wai2(WMN_cR):
    'lIj26RHZ8_3B45_069Kw4_0__m'
    _check_nums(WMN_cR)
    qMV_()
    zK_77D05_.forward(WMN_cR)

@builtin(((('ba' + 'ck') + ('w' + 'ar')) + chr((51 + 49))), ((chr(98) + ('' + 'ac')) + chr(107)), ('' + (chr(98) + 'k')))
def qU5V4_(WMN_cR):
    'r0u3_9X_6_riW__8__98cE_h88'
    _check_nums(WMN_cR)
    qMV_()
    zK_77D05_.backward(WMN_cR)

@builtin((('' + ('l' + 'e')) + ('f' + chr(116))), (chr(108) + 't'))
def s_Mk83w(WMN_cR):
    'L_vPT1Ei34OQ7hH5_2G2o'
    _check_nums(WMN_cR)
    qMV_()
    zK_77D05_.left(WMN_cR)

@builtin((('r' + ('i' + 'g')) + (str() + ('h' + 't'))), (str() + (str() + ('' + 'rt'))))
def H83_gOt1(WMN_cR):
    'H23V43j41nt9_2W16X046VO03__'
    _check_nums(WMN_cR)
    qMV_()
    zK_77D05_.right(WMN_cR)

@builtin((chr(99) + (chr(105) + ('rcl' + 'e'))))
def XLPx6_5(r, Gf___1=None):
    'y41u33371o73bq0_3z15e83_645c7'
    if (Gf___1 is None):
        _check_nums(r)
    else:
        _check_nums(r, Gf___1)
    qMV_()
    zK_77D05_.circle(r, (Gf___1 and Gf___1))

@builtin(((('' + 'setposi') + ('' + 'tio')) + chr((98 + 12))), (('' + ('' + 'setpo')) + 's'), (('' + ('g' + 'ot')) + chr((178 + -67))))
def L_5j63(x, y):
    'V56__LCv___47_Eh29kC_z34h_7v'
    _check_nums(x, y)
    qMV_()
    zK_77D05_.setposition(x, y)

@builtin((('s' + ('e' + 't')) + (('hea' + 'd') + ('in' + 'g'))), ((str() + ('s' + 'e')) + ('t' + chr(104))))
def d9_1b_DG_(V_398h4U):
    'h53r01a__U35__392X21L1H38o3'
    _check_nums(V_398h4U)
    qMV_()
    zK_77D05_.setheading(V_398h4U)

@builtin((chr(112) + (('e' + 'nu') + 'p')), (chr((61 + 51)) + 'u'))
def d9__QN_():
    'BiR15_0m5m28tp_I4_6eN_1V'
    qMV_()
    zK_77D05_.penup()

@builtin((('' + ('pend' + 'ow')) + chr(110)), (chr((122 + -10)) + 'd'))
def T2rS50q():
    'KezI77ju8VYr4827t_laW7U3jr'
    qMV_()
    zK_77D05_.pendown()

@builtin(((('s' + 'h') + ('owt' + 'u')) + ('' + ('r' + 'tle'))), (chr((27 + 88)) + chr((55 + 61))))
def o6Fu_O_1_():
    't_c4O58z22v63EGv_vW6_c4B'
    qMV_()
    zK_77D05_.showturtle()

@builtin(((('hi' + 'd') + ('etu' + 'rt')) + (chr(108) + 'e')), (str() + (chr(104) + chr(116))))
def WN6v0S6b8():
    'h2166U96Dv1Y_72J1__W7'
    qMV_()
    zK_77D05_.hideturtle()

@builtin(((str() + ('c' + 'l')) + (('' + 'ea') + chr(114))))
def M4d16u9():
    'dq6F_MzrzM_wH52279U_5TODnN_'
    qMV_()
    zK_77D05_.clear()

@builtin(((('' + 'co') + chr(108)) + (str() + ('' + 'or'))))
def r_WLQ77(a2876):
    'O6e63w44D_0_W34Jj8___11'
    qMV_()
    validate_type(a2876, scheme_stringp, 0, (str() + (chr(99) + ('' + 'olor'))))
    zK_77D05_.color(eval(a2876))

@builtin(((str() + ('' + 'rg')) + 'b'))
def e7Pl9Lyi(y__2L3Z3, j91oLb8_, B0Neg4_77):
    'V636U04l1Yb_1_bI4I1h'
    C3_wMBJD = (y__2L3Z3, j91oLb8_, B0Neg4_77)
    for x in C3_wMBJD:
        if ((x < int(((0.15635501037922406 + 0.8221893627668928) * 0))) or (x > (((-97 + -2) + (-29 + 45)) + ((68 + -64) + (3 + 77))))):
            raise SchemeError((((('I' + 'l') + 'l') + (('' + 'egal colo') + ('r i' + 'ntensity in '))) + repl_str(C3_wMBJD)))
    yPUM_G98_ = tuple((int((x * (((358 + -69) + (-72 + 61)) + ((-29 + 92) + (-156 + 70))))) for x in C3_wMBJD))
    return (((('"#' + '%02x%02') + ('x%' + '0')) + ('2' + ('x' + '"'))) % yPUM_G98_)

@builtin(((('' + 'begi') + ('n_fi' + 'l')) + chr((151 + -43))))
def m47_zR_uz():
    'Deb_d20w2W5_7FHw8HpcKUt'
    qMV_()
    zK_77D05_.begin_fill()

@builtin((chr((55 + 46)) + (('' + 'nd') + ('' + '_fill'))))
def o___F3As():
    'aK61K1_70D_gI_1__76_'
    qMV_()
    zK_77D05_.end_fill()

@builtin(((chr(98) + ('gcol' + 'o')) + chr(114)))
def z_23Sl84(a2876):
    qMV_()
    validate_type(a2876, scheme_stringp, int((((-1.2344200490831936 + 0.9680931438596627) + (0.6540933370856364 + 0.18557963392316523)) * 0)), (chr((83 + 15)) + (('g' + 'colo') + chr(114))))
    zK_77D05_.bgcolor(eval(a2876))

@builtin(((('ex' + 'i') + 't') + (('o' + 'n') + ('cl' + 'ick'))))
def EjjjvfGj_():
    global zK_77D05_
    'n8f6rRJ_K_52y__M50eZr_z69j_q'
    if (zK_77D05_ is None):
        return
    qMV_()
    if builtins.TK_TURTLE:
        print(((('Close or cli' + 'ck on turtle ') + 'w') + (('indo' + 'w to com') + ('plet' + 'e exit'))))
    if (builtins.TURTLE_SAVE_PATH is not None):
        GA1r(builtins.TURTLE_SAVE_PATH)
    zK_77D05_.exitonclick()
    zK_77D05_ = None

@builtin((chr((29 + 86)) + (('p' + 'e') + ('' + 'ed'))))
def Sus9d4(s):
    'G__3134X7_N_40I_j2lV'
    validate_type(s, scheme_integerp, 0, ((str() + ('s' + 'pe')) + (chr(101) + chr(100))))
    qMV_()
    zK_77D05_.speed(s)

@builtin((str() + (chr(112) + ('i' + 'xel'))))
def x__M5(x, y, a2876):
    'G_9H_8I4_U0__134yXreM5_'
    validate_type(a2876, scheme_stringp, int((((-0.3315196025150776 + 0.5434144386667508) + (-0.004738509426625459 + 0.1880947564029991)) * int(((-0.29852711493860284 + 0.9422191905429516) * 0)))), ((('' + 'pix') + 'e') + chr(108)))
    j_458c5_b = a2876[(((98 + 35) + (-143 + 69)) + ((-30 + -96) + (118 + -50))):(- (((-61 + -44) + (21 + 47)) + ((113 + -94) + (-34 + 53))))]
    qMV_()
    zK_77D05_.pixel(x, y, j_458c5_b)

@builtin((chr((87 + 25)) + (('ixe' + 'ls') + ('i' + 'ze'))))
def o3az1w_5(gFKa):
    'U_3_b03_263_1_3D9hfTN_I4V3w'
    _check_nums(gFKa)
    qMV_()
    zK_77D05_.pixel_size(gFKa)

@builtin((str() + (('sc' + 'reen_widt') + 'h')))
def xP5n6():
    'irF_V2I6584624G95hU_BKPK0'
    qMV_()
    return zK_77D05_.canvas_width()

@builtin(((('s' + 'cr') + ('een_h' + 'ei')) + (('g' + 'h') + chr(116))))
def Ygf___a3():
    'b0tlQt41mwv_9_7ED_5dX'
    qMV_()
    return zK_77D05_.canvas_height()

def GA1r(al7532O):
    if (not builtins.TK_TURTLE):
        al7532O = (al7532O + (str() + (str() + ('.p' + 'ng'))))
        t_9H5Y_.export().save(al7532O, (chr((155 + -43)) + (str() + ('' + 'ng'))))
    else:
        t_9H5Y_.export((al7532O + (('.' + chr(112)) + chr(115))))

@builtin(((('sa' + 've-t') + ('o' + '-')) + (('f' + 'i') + ('' + 'le'))))
def fk3mb_I2_(al7532O):
    qMV_()
    validate_type(al7532O, scheme_stringp, int((((-0.6608555559524587 + 0.22069290993716384) + (0.7247823955161498 + 0.10647500552724287)) * 0)), (str() + (('sav' + 'e-to') + ('-fil' + 'e'))))
    al7532O = eval(al7532O)
    GA1r(al7532O)

@builtin(((('pri' + 'nt-t') + ('hen-retu' + 'r')) + chr((33 + 77))))
def k_QC_(val1, nslxb7z):
    print(repl_str(val1))
    return nslxb7z
'aeXds8k0_2J8_72OQ7_1k197'
m__28M6z4 = (set((chr(48) + (('1' + '234') + ('5678' + '9')))) | set((('+' + chr(45)) + chr((-33 + 79)))))
f806X_ = (((set((('' + ('' + '!$%&')) + (('*' + '/:<=>?@^_') + '~'))) | set(((('' + 'ab') + chr(99)) + (('defghijkl' + 'm') + ('no' + 'pqrstuvwxyz'))))) | set(((('ABCDE' + 'FGHIJK') + ('LMNOPQRSTUV' + 'WXY')) + chr((181 + -91))))) | m__28M6z4)
o314_t = set(chr((82 + -48)))
U_bhM359 = set(((str() + ('' + ' \t')) + (chr(10) + chr(13))))
aHw_7mlE = set(((('' + '()') + ('' + "[]'")) + chr((193 + -97))))
tT4B_65 = (((U_bhM359 | aHw_7mlE) | o314_t) | {chr((28 + 16)), (str() + (chr(44) + chr(64)))})
s_L9hHL = (aHw_7mlE | {chr((-12 + 58)), chr(((37 + -27) + (-25 + 59))), (str() + (',' + '@'))})
n792TL6y3 = (((249 + -75) + (-168 + 87)) + ((-74 + -28) + (-26 + 85)))

def I8__60_(*uV528):
    for iter in uV528:
        (yield from iter)

def Y2u_Q8(s):
    'CY_7_s1016Wg0hnN4V5_f'
    if (len(s) == int(((0.5591757003874898 + 0.41385486359592694) * 0))):
        return False
    for a2876 in s:
        if (a2876 not in f806X_):
            return False
    return True

def z99532_C(m_2XuJE, FROeY_5):
    'YKHBEkj83_g3G_S__81UB488'
    while (FROeY_5 < len(m_2XuJE)):
        a2876 = m_2XuJE[FROeY_5]
        if (a2876 == chr(((91 + 53) + (-42 + -43)))):
            return (None, len(m_2XuJE))
        elif (a2876 in U_bhM359):
            FROeY_5 += (((231 + -74) + (-73 + -26)) + ((30 + -41) + (-68 + 22)))
        elif (a2876 in aHw_7mlE):
            'cBu_Kc12O_X_7e6n5d7a'
            return (a2876, (FROeY_5 + (((-6 + -14) + (-62 + -2)) + ((235 + -53) + (-57 + -40)))))
        elif (a2876 == chr((67 + -32))):
            return (m_2XuJE[FROeY_5:(FROeY_5 + (((43 + -75) + (23 + -28)) + ((-26 + 1) + (105 + -41))))], min((FROeY_5 + (((20 + 9) + (-1 + 15)) + ((15 + -45) + (-31 + 20)))), len(m_2XuJE)))
        elif (a2876 == chr(((-91 + 98) + (-37 + 74)))):
            if (((FROeY_5 + (((-1 + -46) + (3 + 48)) + ((92 + -99) + (-33 + 37)))) < len(m_2XuJE)) and (m_2XuJE[(FROeY_5 + (((141 + -78) + (-57 + 28)) + ((-57 + 30) + (-81 + 75))))] == chr((-13 + 77)))):
                return ((',' + chr((16 + 48))), (FROeY_5 + (((-82 + -87) + (147 + -52)) + ((-65 + 44) + (5 + 92)))))
            return (a2876, (FROeY_5 + (((-46 + 25) + (42 + -41)) + ((101 + -15) + (-108 + 43)))))
        elif (a2876 in o314_t):
            if (((FROeY_5 + (((82 + -44) + (-16 + 1)) + ((-20 + -92) + (175 + -85)))) < len(m_2XuJE)) and (m_2XuJE[(FROeY_5 + ((0 + (48 + -11)) + ((-78 + 82) + (-109 + 69))))] == a2876)):
                return ((a2876 + a2876), (FROeY_5 + (((-130 + 61) + (-41 + 42)) + ((-93 + 78) + (163 + -78)))))
            s = str()
            FROeY_5 += (((59 + 70) + (44 + -84)) + ((18 + -81) + (-98 + 73)))
            while (FROeY_5 < len(m_2XuJE)):
                a2876 = m_2XuJE[FROeY_5]
                if (a2876 == chr(((154 + -94) + (64 + -90)))):
                    RqybY_35(s, (len(s) + (((-29 + 93) + (-95 + 50)) + ((57 + -61) + (-93 + 80)))))
                    return ((('"' + s) + '"'), (FROeY_5 + (((49 + 4) + (-55 + 29)) + ((25 + -83) + (74 + -42)))))
                elif (a2876 == chr(92)):
                    if ((FROeY_5 + (((38 + 81) + (-13 + -9)) + ((-134 + -15) + (137 + -84)))) == len(m_2XuJE)):
                        raise SyntaxError(((('Str' + 'i') + ('ng end' + 'ed')) + (' ' + ('a' + 'bruptly'))))
                    next = m_2XuJE[(FROeY_5 + (((201 + -69) + (-76 + 11)) + ((-177 + 50) + (115 + -54))))]
                    if (next == chr((204 + -94))):
                        s += chr(((-81 + 80) + (-81 + 92)))
                    else:
                        s += next
                    FROeY_5 += (((40 + -67) + (66 + -76)) + ((35 + 1) + (-82 + 85)))
                else:
                    s += a2876
                    FROeY_5 += (((57 + -60) + (62 + -6)) + ((52 + -43) + (-43 + -18)))
            raise SyntaxError(((('St' + 'ring e') + ('' + 'nde')) + (('' + 'd ab') + ('rupt' + 'ly'))))
        else:
            BnFrx = FROeY_5
            while ((BnFrx < len(m_2XuJE)) and (m_2XuJE[BnFrx] not in tT4B_65)):
                BnFrx += (((-197 + 40) + (140 + -59)) + ((-96 + 78) + (133 + -38)))
            RqybY_35(m_2XuJE[FROeY_5:BnFrx], (min(BnFrx, len(m_2XuJE)) - FROeY_5))
            return (m_2XuJE[FROeY_5:BnFrx], min(BnFrx, len(m_2XuJE)))
    return (None, len(m_2XuJE))

def E2Ut(m_2XuJE):
    'V_N__3746ob6wB57__8H_nm9_D'
    result = []
    (u_8BjZ, i) = z99532_C(m_2XuJE, int((((-0.1971376681772019 + 0.2723902009049476) + (-0.41289755631592107 + 0.9179616957222617)) * int(((-0.07140574552461043 + 0.4515261670333237) * int((0.914719241039301 * 0)))))))
    while (u_8BjZ is not None):
        if (u_8BjZ in s_L9hHL):
            result.append(u_8BjZ)
        elif ((u_8BjZ == (chr((-31 + 66)) + chr(116))) or (u_8BjZ.lower() == (('t' + ('r' + 'u')) + 'e'))):
            result.append(True)
        elif ((u_8BjZ == ('#' + chr((28 + 74)))) or (u_8BjZ.lower() == (chr((149 + -47)) + (('' + 'al') + ('s' + 'e'))))):
            result.append(False)
        elif (u_8BjZ == ('n' + ('' + ('' + 'il')))):
            result.append(u_8BjZ)
        elif (u_8BjZ[int((((-0.07346376825469036 + 0.38540174317057874) + (-0.224539469087371 + 0.6303028156620094)) * int(((0.48607004759418815 + 0.4039533373529466) * int((0.94793600014987 * 0))))))] in f806X_):
            tzb15FPK = False
            if (u_8BjZ[int((((-1.3111886731819051 + 0.6718960839651719) + (0.6689621897852038 + 0.3278849469256877)) * int((0.44858043955671423 * 0))))] in m__28M6z4):
                try:
                    result.append(int(u_8BjZ))
                    tzb15FPK = True
                except ValueError:
                    try:
                        result.append(float(u_8BjZ))
                        tzb15FPK = True
                    except ValueError:
                        pass
            if (not tzb15FPK):
                if Y2u_Q8(u_8BjZ):
                    result.append(u_8BjZ.lower())
                else:
                    raise ValueError(((('' + 'inval') + ('id nume' + 'ra')) + (('l' + ' ') + ('o' + 'r symbol: {0}'))).format(u_8BjZ))
        elif (u_8BjZ[int((0.3173413898783828 * 0))] in o314_t):
            result.append(u_8BjZ)
        else:
            gA85_l63 = [((('wa' + 'r') + ('n' + 'ing: invalid')) + ((' ' + 'tok') + ('en: ' + '{0}'))).format(u_8BjZ), ((chr(((-11 + 45) + (-33 + 31))) * (((-86 + 83) + (-107 + 27)) + ((46 + 4) + (40 + -3)))) + m_2XuJE), ((' ' * (i + (((-111 + 86) + (67 + -50)) + ((67 + -58) + (85 + -82))))) + chr((-4 + 98)))]
            raise ValueError(chr((21 + -11)).join(gA85_l63))
        (u_8BjZ, i) = z99532_C(m_2XuJE, i)
    return result

def RqybY_35(Tz2_gaQr, ea9o):
    if (ea9o > n792TL6y3):
        import warnings as FnU_
        FnU_.warn(((chr(84) + ('oke' + 'n {')) + (('} has exc' + 'eeded th') + ('e maximum token length ' + '{}'))).format(Tz2_gaQr, n792TL6y3, ea9o))

def AD_0Zpkm_(D2gw_i62):
    'te7___jD7Ub5971I9_8CU_t9504GT'
    return (E2Ut(m_2XuJE) for m_2XuJE in D2gw_i62)

def noW76(D2gw_i62):
    'u_89__7B3GVg135psl_v5'
    return len(list(I8__60_(*AD_0Zpkm_(D2gw_i62))))

def run(*args):
    import argparse as argparse
    parser = argparse.ArgumentParser(description=((('Coun' + 't Sche') + ('me' + ' t')) + (('ok' + 'en') + ('' + 's.'))))
    parser.add_argument((str() + ('' + ('' + 'file'))), nargs=chr(((103 + -12) + (-101 + 73))), type=argparse.FileType(chr(((171 + -97) + (140 + -100)))), default=sys.stdin, help=((('input' + ' f') + ('ile to ' + 'be c')) + (('o' + 'unt') + ('' + 'ed'))))
    args = parser.parse_args()
    print((('' + ('c' + 'o')) + (('' + 'unt') + ('' + 'ed'))), noW76(args.file), (str() + (('to' + 'ke') + ('n' + 's'))))
global SPECIAL_FORMS

def scheme_eval(expr, env, _=None):
    'Sg7j7_jEELy5Dnwj046a9AS_3F__'
    env.stack.append(expr)
    if scheme_symbolp(expr):
        result = env.lookup(expr)
        env.stack.pop()
        return result
    elif self_evaluating(expr):
        env.stack.pop()
        return expr
    if (not scheme_listp(expr)):
        raise SchemeError(((('ma' + 'l') + ('for' + 'med list: ')) + (str() + ('{0' + '}'))).format(repl_str(expr)))
    (first, rest) = (expr.first, expr.rest)
    if (scheme_symbolp(first) and (first in SPECIAL_FORMS)):
        result = SPECIAL_FORMS[first](rest, env)
        env.stack.pop()
        return result
    else:
        oprerator = scheme_eval(first, env)
        if isinstance(oprerator, QI0_kY):
            expr = complete_apply(oprerator, rest, env)
            return scheme_eval(expr, env)
        args = rest.map((lambda x: scheme_eval(x, env)))
        result = scheme_apply(oprerator, args, env)
        env.stack.pop()
        return result

def scheme_apply(oprerator, args, env):
    'MB9F274D___3xY__vpNQ_8'
    validate_procedure(oprerator)
    if (not isinstance(env, Frame)):
        assert False, ((('' + 'No') + chr(116)) + (('' + ' a Frame:') + (' ' + '{}'))).format(env)
    if isinstance(oprerator, BuiltinProcedure):
        list_args = []
        while (args is not nil):
            list_args.append(args.first)
            args = args.rest
        if oprerator.need_env:
            list_args.append(env)
        try:
            return oprerator.py_func(*list_args)
        except TypeError as err:
            raise SchemeError(((('in' + 'correc') + ('t num' + 'ber')) + (chr(32) + ('of argu' + 'ments: {0}'))).format(oprerator))
    elif isinstance(oprerator, LambdaProcedure):
        child_frame = oprerator.env.make_child_frame(oprerator.formals, args)
        return eval_all(oprerator.body, child_frame)
    elif isinstance(oprerator, MuProcedure):
        child_frame = env.make_child_frame(oprerator.formals, args)
        return eval_all(oprerator.body, child_frame)
    else:
        assert False, ((('Unexpec' + 'ted') + (' ' + 'pr')) + (('oc' + 'edu') + ('re: ' + '{}'))).format(oprerator)

def eval_all(expressions, env):
    'i6793Z174_3hKOq_9F_HhZ'
    value = None
    while (expressions is not nil):
        tail = (expressions.rest is nil)
        value = scheme_eval(expressions.first, env, tail)
        expressions = expressions.rest
    return value

class Unevaluated():
    'n9L_RzH6i9100BiT9kk0r_2'

    def __init__(self, expr, env):
        'sx_Z11o4mk8rd5h6x5Am'
        self.expr = expr
        self.env = env

def complete_apply(oprerator, args, env):
    'vD3T_69HPQa_m_9_5_D_'
    validate_procedure(oprerator)
    val = scheme_apply(oprerator, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val

def optimize_tail_calls(unoptimized_scheme_eval):
    'RF5157264Y2_6_62y2oa_U4Xf'

    def optimized_eval(expr, env, tail=False):
        'C882NG6H0sC_6429l2_M6'
        if (tail and (not scheme_symbolp(expr)) and (not self_evaluating(expr))):
            return Unevaluated(expr, env)
        result = Unevaluated(expr, env)
        while isinstance(result, Unevaluated):
            result = unoptimized_scheme_eval(result.expr, result.env)
        return result
    return optimized_eval
if ((('' + ('do' + 'cte')) + ('' + ('' + 'st'))) not in sys.argv[int((((-0.7976968351371473 + 0.9329686565382934) + (-0.2812426917424419 + 0.47281977183737733)) * int(((0.740388285497075 + 0.18970529680919312) * int((0.900174788653162 * 0))))))]):
    scheme_eval = optimize_tail_calls(scheme_eval)

class SchemeError(Exception):
    'Myf9G_0r__sDOCe5488750_'

class Frame():
    'SPC__S_00I08_A9K85611gWjb'

    def __init__(self, parent):
        'C_a_2_Yt59V_3_R4P8_nD2'
        self.bindings = {}
        self.parent = parent
        if self.parent:
            self.stack = self.parent.stack
        else:
            self.stack = []

    def __repr__(self):
        if (self.parent is None):
            return (str() + (('' + '<Gl') + ('obal Fra' + 'me>')))
        s = sorted([(chr((177 + -54)) + ('' + ('0}: ' + '{1}'))).format(FROeY_5, v) for (FROeY_5, v) in self.bindings.items()])
        return ((('' + '<{{') + ('{0}' + '}} ->')) + ((' {' + '1}') + '>')).format((',' + ' ').join(s), repr(self.parent))

    def define(self, symbol, value):
        'sF_8c1ow0m12s0Hr_1148S0_757D'
        self.bindings[symbol] = value

    def lookup(self, symbol):
        'DB5_XZ56Gxc4_1_I_fX_6m4FK'
        e = self
        while (e is not None):
            if (symbol in e.bindings):
                return e.bindings[symbol]
            e = e.parent
        raise SchemeError((('' + ('u' + 'nkno')) + (('wn identif' + 'i') + ('er: {0' + '}'))).format(symbol))

    def e003HAek(self, symbol, value):
        'c__98_M7PEw__F_e41U1_p39zE'
        e = self
        while (e is not None):
            if (symbol in e.bindings):
                e.define(symbol, value)
                return
            e = e.parent
        raise SchemeError(((('unknown' + ' iden') + ('tifier' + ': {')) + ('0' + chr(125))).format(symbol))

    def make_child_frame(self, formals, vals):
        'I_244T_xOY856Y_lOA1W077s0g_'
        if (len(formals) != len(vals)):
            raise SchemeError(((('Incorrect' + ' number ') + ('' + 'of')) + ((' arguments to' + ' funct') + ('ion' + ' call'))))
        child = Frame(self)
        while ((formals != nil) and (vals != nil)):
            if ev473(formals.first):
                assert (formals.rest is nil), ((('should hav' + 'e ') + ('' + 'be')) + (('en caught ' + 'ea') + ('' + 'rlier')))
                child.define(aLn9U(formals.first), vals)
                return child
            if (vals is nil):
                raise SchemeError(((('too ' + 'few') + ('' + ' argu')) + (('ments ' + 'to function c') + ('al' + 'l'))))
            child.define(formals.first, vals.first)
            (formals, vals) = (formals.rest, vals.rest)
        if ((formals != nil) and ev473(formals.first)):
            assert (formals.rest is nil), ((('' + 'sho') + ('uld' + ' have be')) + (('en caug' + 'ht earl') + ('' + 'ier')))
            child.define(aLn9U(formals.first), vals)
            return child
        if ((formals != nil) or (vals != nil)):
            raise SchemeError(((('I' + 'nc') + ('o' + 'r')) + (('rect ' + 'number of argum') + ('ents to fu' + 'nction call'))))
        if (formals != nil):
            child.define(formals, vals)
        elif (vals != nil):
            raise SchemeError(((('too many argu' + 'm') + ('en' + 'ts to function c')) + (chr(97) + ('' + 'll'))))
        return child

class Procedure():
    'a14T_8_0usEv37bn91p_A9'

class BuiltinProcedure(Procedure):
    'j_LnF_3A48ld43ERJVnI'

    def __init__(self, py_func, need_env=False, name='builtin'):
        self.name = name
        self.py_func = py_func
        self.need_env = need_env

    def __str__(self):
        return (chr((90 + -55)) + ('' + ('[' + '{0}]'))).format(self.name)

class LambdaProcedure(Procedure):
    'pZ3R8_4IX_a8Ry797a_F'
    name = ('' + (('[lamb' + 'd') + ('' + 'a]')))

    def __init__(self, formals, body, env):
        'M__ET9pX3H6_9r_B8TgV29_r_'
        assert isinstance(env, Frame), ((('e' + 'nv m') + ('ust' + ' be')) + ((' o' + 'f t') + ('ype Fr' + 'ame')))
        validate_type(formals, scheme_listp, int((0.2939893996413272 * 0)), ((('Lamb' + 'da') + 'P') + (('roced' + 'u') + ('' + 're'))))
        validate_type(body, scheme_listp, (((66 + -78) + (-48 + 29)) + ((-38 + 78) + (72 + -80))), ((chr(76) + ('am' + 'bdaPr')) + (chr(111) + ('ce' + 'dure'))))
        self.formals = formals
        self.body = body
        self.env = env

    def __str__(self):
        return str(Pair(((str() + ('lam' + 'bd')) + 'a'), Pair(self.formals, self.body)))

    def __repr__(self):
        return ((('' + 'La') + ('m' + 'bdaProcedu')) + (('re' + '({0},') + (' {1},' + ' {2})'))).format(repr(self.formals), repr(self.body), repr(self.env))

class MuProcedure(Procedure):
    'V5723g47C__80030LwS_0s8sd'
    name = ((chr(91) + ('' + 'mu')) + ']')

    def __init__(self, formals, body):
        'E2X_5202COX6aNN_fS24BX_q55U'
        self.formals = formals
        self.body = body

    def __str__(self):
        return str(Pair(('m' + chr((42 + 75))), Pair(self.formals, self.body)))

    def __repr__(self):
        return ((str() + ('M' + 'uPr')) + (('' + 'ocedu') + ('re({0}' + ', {1})'))).format(repr(self.formals), repr(self.body))

class QI0_kY(LambdaProcedure):
    'PQCZ30Y_OlkT56P1W_CD0'

class Promise():
    'Ks_918_9j__2WR1e__34V_1'

    def __init__(self, expression, env):
        self.expression = expression
        self.env = env

    def evaluate(self):
        if (self.expression is not None):
            value = scheme_eval(self.expression, self.env)
            if ((not builtins.DOTS_ARE_CONS) and (not ((value is nil) or isinstance(value, Pair)))):
                raise SchemeError((((('result o' + 'f forcing a promise should be a ') + ('' + 'pair o')) + (('r n' + 'il, but') + (' w' + 'as %s'))) % value))
            self.value = value
            self.expression = None
        return self.value

    def __str__(self):
        return ((('#[promise ' + '(') + ('' + '{0')) + (('}fo' + 'r') + ('c' + 'ed)]'))).format(((str() + (('n' + 'ot') + ' ')) if (self.expression is not None) else ''))

def do_define_form(expressions, env):
    'VZ_71k8I59b7_iTnx_2_u__1_Sx_'
    validate_form(expressions, (((28 + -81) + (-119 + 91)) + ((186 + -51) + (-46 + -6))))
    signature = expressions.first
    if scheme_symbolp(signature):
        validate_form(expressions, (((114 + 48) + (-4 + -94)) + ((-10 + -27) + (11 + -36))), (((-47 + 34) + (0 + -39)) + ((6 + -37) + (111 + -26))))
        value = scheme_eval(expressions.rest.first, env)
        env.define(signature, value)
        return signature
    elif (isinstance(signature, Pair) and scheme_symbolp(signature.first)):
        name = signature.first
        formals = signature.rest
        body = expressions.rest
        value = do_lambda_form(Pair(formals, body), env)
        value.name = name
        env.define(name, value)
        return name
    else:
        XJiqF6 = (signature.first if isinstance(signature, Pair) else signature)
        raise SchemeError(((('non-sym' + 'b') + ('' + 'ol')) + ((':' + ' {') + ('' + '0}'))).format(XJiqF6))

def do_quote_form(expressions, env):
    'S85oQmY3hVM02_7_3H2B832'
    validate_form(expressions, (((-148 + 93) + (-80 + 81)) + ((108 + -80) + (62 + -35))), (((42 + 7) + (-57 + 59)) + ((-17 + -29) + (58 + -62))))
    return expressions.first

def do_begin_form(expressions, env):
    'D4__7C972t0E59XrA06Q'
    validate_form(expressions, (((40 + -23) + (-140 + 71)) + ((59 + -32) + (-22 + 48))))
    return eval_all(expressions, env)

def do_lambda_form(expressions, env):
    'D3_09DD3n8IaNF1yOED_C5n78'
    validate_form(expressions, (((149 + -96) + (-99 + 79)) + ((108 + -41) + (-197 + 99))))
    formals = expressions.first
    validate_formals(formals)
    return LambdaProcedure(formals, expressions.rest, env)

def do_if_form(expressions, env):
    'X9Y08_0_QL0_6922kJ_2t482_L3'
    validate_form(expressions, (((150 + -12) + (-8 + -46)) + ((53 + -65) + (18 + -88))), (((-106 + 83) + (24 + -60)) + ((18 + 88) + (11 + -55))))
    if is_scheme_true(scheme_eval(expressions.first, env)):
        return scheme_eval(expressions.rest.first, env, True)
    elif (len(expressions) == (((-14 + -9) + (-79 + 17)) + ((219 + -34) + (-10 + -87)))):
        return scheme_eval(expressions.rest.rest.first, env, True)

def do_and_form(expressions, env):
    'wxG1W82V2_07__o5__9R6A_'
    value = True
    while (expressions is not nil):
        tail = (expressions.rest is nil)
        value = scheme_eval(expressions.first, env, tail)
        if is_scheme_false(value):
            return value
        expressions = expressions.rest
    return value

def do_or_form(expressions, env):
    'W_7BVt_RYe_mW_K6_5__dI_4Q2'
    value = False
    while (expressions is not nil):
        tail = (expressions.rest is nil)
        value = scheme_eval(expressions.first, env, tail)
        if is_scheme_true(value):
            return value
        expressions = expressions.rest
    return value

def do_cond_form(expressions, env):
    'W16t25_R1p_Wbs3P7D94a'
    while (expressions is not nil):
        clause = expressions.first
        validate_form(clause, (((43 + -94) + (32 + -12)) + ((83 + -53) + (53 + -51))))
        if (clause.first == (str() + ('e' + ('l' + 'se')))):
            test = True
            if (expressions.rest != nil):
                raise SchemeError(((('' + 'el') + ('se' + ' ')) + (('m' + 'ust ') + ('be las' + 't'))))
        else:
            test = scheme_eval(clause.first, env)
        if is_scheme_true(test):
            if (len(clause) == (((-71 + 28) + (-40 + 60)) + ((-62 + 61) + (4 + 21)))):
                return test
            else:
                return eval_all(clause.rest, env)
        expressions = expressions.rest

def do_let_form(expressions, env):
    'OPu2S6d5f0Y0I3g0g_AX0_Lg2_'
    validate_form(expressions, (((-48 + -42) + (-9 + 11)) + ((195 + -69) + (-28 + -8))))
    let_env = make_let_frame(expressions.first, env)
    return eval_all(expressions.rest, let_env)

def make_let_frame(bindings, env):
    'Ht25_12_jL9_0__2J5C1_S69I'
    if (not scheme_listp(bindings)):
        raise SchemeError((('b' + ('ad bindings' + ' list in let f')) + (('' + 'or') + 'm')))
    name = vals = nil
    while (bindings is not nil):
        VzmTN = bindings.first
        validate_form(VzmTN, (((-55 + 50) + int((0.6915818891895422 * 0))) + ((85 + -68) + (18 + -28))), (((136 + 10) + (-85 + -12)) + ((24 + -20) + (-129 + 78))))
        name = VzmTN.first
        val = scheme_eval(VzmTN.rest.first, env)
        name = Pair(name, name)
        vals = Pair(val, vals)
        bindings = bindings.rest
    validate_formals(name)
    return env.make_child_frame(name, vals)

def do_define_marco_form(expressions, env):
    'C7R_376TQ6224N_9tFP51_5_gZ7'
    validate_form(expressions, (((-178 + 93) + (77 + -35)) + ((167 + -91) + (56 + -87))))
    rPt_ajbd = expressions.first
    if (isinstance(rPt_ajbd, Pair) and scheme_symbolp(rPt_ajbd.first)):
        name = rPt_ajbd.first
        formals = rPt_ajbd.rest
        body = expressions.rest
        validate_formals(formals)
        value = QI0_kY(formals, body, env)
        value.name = name
        env.define(name, value)
        return name
    else:
        raise SchemeError(((('' + 'improper fo') + ('rm for defi' + 'ne-mac')) + (str() + ('r' + 'o'))))

def do_quasiquote_form(expressions, env):
    'j_58i5V19_UB_b458_gy89_'

    def quasiquote_item(val, env, level):
        'YwUZ2Z7W7YOxGD95___r_1g'
        if (not scheme_pairp(val)):
            return val
        if (val.first == ((chr(117) + ('nq' + 'u')) + (chr(111) + ('' + 'te')))):
            level -= (((23 + -79) + (-62 + 98)) + ((93 + 10) + (-60 + -22)))
            if (level == int((((0.03847378731315454 + 0.28445742135821983) + (0.07572007353030108 + 0.1721969044667988)) * int(((0.26869056427739557 + 0.5870260260285749) * 0))))):
                expressions = val.rest
                validate_form(expressions, (((-244 + 76) + (127 + -45)) + ((-83 + 86) + (-3 + 87))), (((-153 + 27) + (-57 + 93)) + ((279 + -92) + (-135 + 39))))
                return scheme_eval(expressions.first, env)
        elif (val.first == (('q' + ('uas' + 'iquo')) + (str() + ('t' + 'e')))):
            level += (((-49 + -26) + (-99 + 80)) + ((171 + -24) + (16 + -68)))
        return val.map((lambda elem: quasiquote_item(elem, env, level)))
    validate_form(expressions, (((-134 + 83) + (-61 + 69)) + ((154 + -21) + (-101 + 12))), (((52 + 34) + (-34 + 19)) + ((-99 + 12) + (24 + -7))))
    return quasiquote_item(expressions.first, env, (((-41 + 72) + (46 + -66)) + ((-5 + -91) + (24 + 62))))

def do_unquote(expressions, env):
    raise SchemeError(((('unq' + 'uot') + 'e') + (('' + ' outside of qu') + ('asiq' + 'uote'))))

def do_mu_form(expressions, env):
    'Il1wh9xv34VH16Ei13s85e_'
    validate_form(expressions, (((11 + 39) + (59 + -53)) + ((-96 + 92) + (-66 + 16))))
    formals = expressions.first
    validate_formals(formals)
    return MuProcedure(formals, expressions.rest)

def M_0j_v(expressions, env):
    'zk97m_O__0__Nxk_iA2x7N_d'
    validate_form(expressions, (((157 + -19) + (-124 + 27)) + ((14 + 2) + (-9 + -47))), (((148 + -67) + (-49 + 45)) + ((-87 + 17) + (-100 + 94))))
    return Promise(expressions.first, env)

def mc204(expressions, env):
    'Q_c40B1vErzC9v15__6_TX9q9p'
    validate_form(expressions, (((-147 + 43) + (42 + 48)) + ((72 + -9) + (27 + -74))), (((107 + -53) + (-23 + -36)) + ((137 + -67) + (-41 + -22))))
    return Pair(scheme_eval(expressions.first, env), M_0j_v(expressions.rest, env))

def j3y07(s, EB1Tdm75=4):
    return chr(10).join((((' ' * EB1Tdm75) + m_2XuJE) for m_2XuJE in s.split(chr(((-125 + 65) + (96 + -26))))))

def k0p6(expressions, env):
    'DF4619X92Z4_1x___J_27zj8_'
    validate_form(expressions, (((30 + -76) + (72 + -21)) + ((-20 + -11) + (-32 + 60))))
    name = expressions.first
    if (not scheme_symbolp(name)):
        raise SchemeError((((str() + ('' + 'bad ')) + ('' + ('argumen' + 't: '))) + repl_str(name)))
    value = scheme_eval(expressions.rest.first, env)
    env.e003HAek(name, value)

def rhebashnt(expressions, env):
    'JL8i8__1Y89UF_TpS80ki5__4e47'
    validate_form(expressions, (((41 + -74) + (16 + 70)) + ((-129 + 17) + (82 + -22))), (((153 + 3) + (10 + -92)) + ((-138 + 61) + (13 + -9))))

    def egsrzdfhgng(val, level=1):
        'fWu6_859Iah_X6469uG939C_'
        if scheme_pairp(val):
            if (val.first in ((('u' + 'n') + (str() + ('quot' + 'e'))), (('u' + ('nquot' + 'e-spl')) + (('i' + 'c') + ('in' + 'g'))))):
                level -= (((-39 + 8) + (55 + -91)) + ((122 + -85) + (34 + -3)))
                if (level == 0):
                    expressions = val.rest
                    validate_form(expressions, (((-8 + 2) + (-7 + 19)) + ((-135 + 49) + (43 + 38))), (((-62 + -75) + (-14 + 88)) + ((104 + 37) + (-36 + -41))))
                    a7V46_U_ = scheme_eval(expressions.first, env)
                    H_F_ = (val.first == (('' + ('un' + 'quot')) + (('e-' + 'sp') + ('lic' + 'ing'))))
                    if (H_F_ and (not scheme_listp(a7V46_U_))):
                        msg = ((('unquote-splic' + 'ing us') + ('e' + 'd on ')) + (str() + ('non-list: {0' + '}')))
                        raise SchemeError(msg.format(a7V46_U_))
                    return (a7V46_U_ if H_F_ else Pair(a7V46_U_, nil))
            elif (val.first == (('' + ('qu' + 'asiquo')) + ('t' + 'e'))):
                level += (((82 + -60) + (-47 + -28)) + ((-83 + 73) + (45 + 19)))
            return Pair(val.s_bEA7fo8((lambda elem: egsrzdfhgng(elem, level))), nil)
        else:
            return Pair(val, nil)
    if (scheme_pairp(expressions.first) and (expressions.first.first == ((('' + 'un') + chr(113)) + (('u' + 'ote-s') + ('plicin' + 'g'))))):
        msg = (('' + ('unquot' + 'e-splicing not ')) + (('in li' + 'st templat') + ('e: {' + '0}')))
        raise SchemeError(msg.format(expressions.first))
    return egsrzdfhgng(expressions.first).first

def C_040e_8(expressions, env):
    raise SchemeError(((('Cannot evalu' + 'at') + ('' + 'e v')) + (('ari' + 'ad') + ('ic s' + 'ymbol'))))

def E8a3635(env):
    try:
        env.lookup(((('_' + '_run_') + ('all_d' + 'oc')) + (('' + 'te') + ('' + 'sts'))))
        return True
    except SchemeError:
        return False

def E_6k__h7r(expressions, env):
    validate_form(expressions, (((-42 + -98) + (42 + 41)) + ((133 + -69) + (-103 + 98))), (((-62 + -65) + (-8 + 97)) + ((58 + -84) + (113 + -47))))
    D88S3wv_1 = E8a3635(env)
    v639 = []
    NdQ55 = v639.append
    x_Q_g3k3_ = False
    try:
        pe_73 = env.stack[:]
        env.stack[:] = []
        z8K_3 = scheme_eval(expressions.first, env)
    except Exception as e:
        NdQ55(((str() + ('Te' + 'st')) + ((' faile' + 'd') + ':')))
        NdQ55(j3y07((((chr(115) + chr(99)) + (('m' + '>') + ' ')) + repl_str(expressions.first)), EB1Tdm75=(((25 + -62) + (28 + -32)) + ((48 + 27) + (31 + -61)))))
        NdQ55((str() + (str() + ('Exp' + 'ected:'))))
        NdQ55(j3y07(repl_str(expressions.rest.first), EB1Tdm75=(((7 + 13) + (-101 + 71)) + ((15 + 10) + (-1 + -10)))))
        NdQ55((('R' + chr(101)) + (('c' + 'ei') + ('v' + 'ed:'))))
        traceback(env, NdQ55)
        NdQ55(((str() + ('' + ('Error' + ': '))) + str(e)))
    else:
        if scheme_equalp(z8K_3, expressions.rest.first):
            x_Q_g3k3_ = True
            NdQ55(((((((('sc' + 'm') + '>') + chr((0 + 32))) + repl_str(expressions.first)) + (str() + (('; rec' + 'eive') + ('d' + ' ')))) + repl_str(expressions.rest.first)) + (('' + (',' + ' suc')) + ('' + ('ce' + 'ss')))))
        else:
            NdQ55(((('T' + 'es') + chr(116)) + (('' + ' failed') + chr(58))))
            NdQ55(j3y07(((chr(115) + (chr(99) + ('' + 'm> '))) + repl_str(expressions.first)), EB1Tdm75=(((-17 + 28) + (19 + -71)) + ((-79 + 38) + (17 + 69)))))
            NdQ55(((('' + 'Exp') + ('' + 'ecte')) + (chr(100) + chr(58))))
            NdQ55(j3y07(repl_str(expressions.rest.first), EB1Tdm75=(((-2 + 45) + (25 + 18)) + ((111 + -93) + (-163 + 63)))))
            NdQ55(((('R' + 'e') + chr(99)) + ('' + ('eive' + 'd:'))))
            NdQ55(j3y07(repl_str(z8K_3)))
    finally:
        env.stack[:] = pe_73
    if D88S3wv_1:
        print((((('D' + 'O') + ('CT' + 'E')) + ('' + ('S' + 'T: '))) + e_7k3iK_3(dict(name=[(chr(68) + (chr(111) + ('cte' + 'sts'))), repl_str(expressions.first)], rawName=(((('Do' + 'c') + ('' + 'test')) + (chr(115) + ('' + ' > '))) + repl_str(expressions.first)), x_Q_g3k3_=x_Q_g3k3_, code=[repl_str(expressions.first)], v639=chr(((-21 + 42) + (19 + -30))).join(v639)))), end=str())
    elif x_Q_g3k3_:
        print(chr(((-68 + 66) + (76 + -64))).join(v639))
    else:
        print('\n'.join(v639), file=sys.stderr)

def Eb_5i6(expressions, env):
    validate_form(expressions, (((-106 + 99) + (-45 + 67)) + ((-86 + 11) + (-1 + 62))), (((-123 + -30) + (43 + 48)) + ((22 + 7) + (-2 + 36))))
    V3lqE9((str() + ('#' + ' ')))
    iFoiu_9P(scheme_eval(expressions.first, env))
SPECIAL_FORMS = {('a' + ('' + ('n' + 'd'))): do_and_form, ((chr(98) + ('e' + 'g')) + ('' + ('i' + 'n'))): do_begin_form, (str() + (('c' + 'o') + ('' + 'nd'))): do_cond_form, (chr(100) + ('e' + ('' + 'fine'))): do_define_form, (str() + (chr(105) + 'f')): do_if_form, ((('la' + 'm') + ('' + 'bd')) + 'a'): do_lambda_form, (str() + (str() + ('le' + 't'))): do_let_form, (chr(111) + chr(114)): do_or_form, ((str() + ('q' + 'uot')) + chr((184 + -83))): do_quote_form, ((str() + ('qu' + 'a')) + (('' + 'siquot') + 'e')): do_quasiquote_form, (chr((170 + -53)) + (('n' + 'quot') + 'e')): do_unquote, ('' + (chr(109) + 'u')): do_mu_form, (chr((22 + 78)) + (('' + 'ef') + ('ine-macr' + 'o'))): do_define_marco_form, ((('' + 'cons') + chr(45)) + (chr(115) + ('tr' + 'eam'))): mc204, (str() + ('d' + ('el' + 'ay'))): M_0j_v, (chr(115) + (str() + ('e' + 't!'))): k0p6, ((('u' + 'nq') + ('' + 'uote-s')) + ('' + ('pli' + 'cing'))): do_unquote, ((('v' + 'a') + 'r') + ('i' + ('ad' + 'ic'))): C_040e_8, (str() + (('exp' + 'ec') + 't')): E_6k__h7r, chr(((-67 + 5) + (175 + -80))): Eb_5i6}
't_tHe6E4lyn_v4825C623X74469a'
__version__ = ((chr(49) + ('.' + '2')) + (chr(46) + '5'))
sys.path.append(((('s' + 'c') + ('he' + 'me')) + (('' + '_re') + ('ad' + 'er'))))
builtins.DOTS_ARE_CONS = True
builtins.TK_TURTLE = False
builtins.TURTLE_SAVE_PATH = None

def read_eval_print_loop(next_line, env, interactive=False, quiet=False, startup=False, load_files=(), report_errors=False):
    'h_X5_5_LEbkM64Y73z0ik9l8z25F9'
    if startup:
        try:
            scheme_load((str() + ('' + ('s' + 'cheme_lib'))), True, env)
        except SchemeError:
            pass
        for filename in load_files:
            scheme_load(filename, True, env)
    while True:
        try:
            src = next_line()
            while src.more_on_line():
                expression = scheme_read(src)
                result = scheme_eval(expression, env)
                if ((not quiet) and (result is not None)):
                    print(repl_str(result))
        except (SchemeError, SyntaxError, ValueError, RuntimeError) as err:
            if report_errors:
                if isinstance(err, SyntaxError):
                    err = SchemeError(err)
                    raise err
            traceback(env)
            if (isinstance(err, RuntimeError) and (((('' + 'maxi') + ('' + 'mum recursion ')) + (('depth ex' + 'ceed') + ('e' + 'd'))) not in getattr(err, (('a' + 'r') + (str() + ('' + 'gs'))))[int(((-0.13676590112293996 + 0.2996157699620351) * 0))])):
                raise
            elif isinstance(err, RuntimeError):
                print(((('E' + 'r') + ('r' + 'or: max')) + (('' + 'imu') + ('m r' + 'ecursion depth exceeded'))))
            else:
                print(('' + (('E' + 'rror') + ':')), err)
        except KeyboardInterrupt:
            if (not startup):
                raise
            env.stack = []
            print()
            print((chr((137 + -62)) + (('ey' + 'bo') + ('' + 'ardInterrupt'))))
            if (not interactive):
                return
        except EOFError:
            print()
            return

def traceback(env, NdQ55=print):
    NdQ55(((('Trac' + 'eb') + ('ack (mo' + 'st recent call ')) + (('l' + 'ast)') + chr(58))))
    for (Q5_t92a1, expr) in enumerate(env.stack):
        NdQ55(((((str() + (str() + ('' + '  '))) + str(Q5_t92a1)) + chr(((-8 + 4) + (-87 + 100)))) + repl_str(expr)))
    env.stack[:] = []

def add_builtins(O945S0M7, funcs_and_names):
    'Uh_Epzi63wU__A_mTF930992U8'
    for (name, py_func, proc_name, need_env) in funcs_and_names:
        O945S0M7.define(name, BuiltinProcedure(py_func, name=proc_name, need_env=need_env))

def create_global_frame():
    'Sr2bs__322p7x_BH86huf31_2B_f'
    env = Frame(None)
    env.define((('' + ('' + 'ev')) + ('a' + 'l')), BuiltinProcedure(scheme_eval, True, ('e' + ('v' + ('' + 'al')))))
    env.define((('a' + ('' + 'ppl')) + chr((207 + -86))), BuiltinProcedure(complete_apply, True, ((chr(97) + 'p') + (str() + ('' + 'ply')))))
    env.define(((('u' + 'nd') + ('e' + 'f')) + (str() + ('i' + 'ned'))), None)
    env.stack = []
    add_builtins(env, BUILTINS)
    return env

def run(*argv):
    import argparse
    parser = argparse.ArgumentParser(description=('' + (('CS 6' + '1A Scheme Interpre') + ('te' + 'r'))))
    import __main__ as dul6_
    if (((chr(108) + chr(111)) + ('g' + ('' + 'ic'))) in dul6_.__file__):
        lN34X4 = ((str() + ('' + 'Logi')) + chr((5 + 94)))
    else:
        lN34X4 = (str() + (str() + ('Sch' + 'eme')))
    version = dul6_.__version__
    parser.add_argument((str() + (('--v' + 'e') + ('' + 'rsion'))), action=((chr(118) + chr(101)) + (('rs' + 'io') + 'n')), version=('' + ('{' + chr(125))).format(version))
    parser.add_argument(((('--' + 'dot') + ('s-ar' + 'e-con')) + chr(115)), action=(chr(115) + (('tor' + 'e_tr') + ('' + 'ue'))), help=((('ru' + 'n with pre-sp19 dotted lis') + ('t' + 's ')) + (('behavior where dots a' + 'r') + ('e c' + 'ons'))))
    parser.add_argument((str() + (('--pillow-tur' + 't') + ('' + 'le'))), action=(('s' + ('t' + 'o')) + (('r' + 'e') + ('_tr' + 'ue'))), help=((('' + 'run with pillow-based') + (' turtle. This is much faster' + ' for')) + (chr(32) + ('rendering but there is' + ' no GUI'))))
    parser.add_argument(((str() + ('--tur' + 'tle-sav')) + (chr(101) + ('-p' + 'ath'))), default=None, help=((('' + 'save the image to this l') + ('oca' + 't')) + (('i' + 'on w') + ('hen don' + 'e'))))
    parser.add_argument(((chr(45) + ('' + 'loa')) + chr((27 + 73))), (str() + ('' + ('-' + 'i'))), action=('' + (('st' + 'ore_') + ('t' + 'rue'))), help=(('r' + ('' + 'un')) + ((' file intera' + 'ct') + ('i' + 'vely'))))
    parser.add_argument((str() + ('f' + ('i' + 'le'))), nargs=chr(((171 + -38) + (13 + -83))), type=argparse.FileType(chr(((131 + 29) + (-22 + -24)))), default=None, help=('S' + (('' + 'ch') + ('em' + 'e file to run'))))
    args = parser.parse_args()
    import builtins
    builtins.TK_TURTLE = (not args.pillow_turtle)
    builtins.TURTLE_SAVE_PATH = args.turtle_save_path
    sys.path.insert(int((((-0.8061631731492233 + 0.4008433683504886) + (0.18471215624011073 + 0.29086504079308206)) * 0)), str())
    next_line = r_k_R9
    interactive = True
    load_files = []
    if (args.file is not None):
        if args.load:
            load_files.append(getattr(args.file, (('' + ('na' + 'm')) + chr(101))))
        else:
            lines = args.file.readlines()

            def next_line():
                return buffer_lines(lines)
            interactive = False
    print((('W' + ('' + 'elcome to the CS 61')) + (('A ' + '{} Interpreter (versio') + ('n' + ' {})'))).format(lN34X4, version))
    read_eval_print_loop(next_line, create_global_frame(), startup=True, interactive=interactive, load_files=load_files)
    EjjjvfGj_()

