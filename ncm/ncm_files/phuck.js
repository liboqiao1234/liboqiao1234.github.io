var constArray = ['getBlob', 'then', 'cwrap', 'metaflac', 'number', 'log', 'ready', 'length', 'BYTES_PER_ELEMENT',
'setValue', '_malloc', 'forEach', 'i32', 'charCodeAt', 'slice', 'buffer', 'setFrame', 'mp3', 'hzHRAmso5InbaxW',
'#14lj_!\x5c]&0U<\x27(', 'ModeOfOperation', 'decode', 'from', 'ecb', 'decrypt', 'hasOwnProperty', 'format',
'flac', 'writeFile', 'input.flac', 'pic', 'hostname', 'join', '--import-picture-from=pic', 'readFile',
'image/jpeg', 'image/png', 'APIC', 'TIT2', 'musicName', 'album', 'artist', 'TPE1', 'addTag'];
(function (_0x28503f, _0x440b3c)
{
    var _0x32bb0f = function (_0x4f5f97)
    {
        while (--_0x4f5f97) {
            _0x28503f['push'](_0x28503f['shift']());
        }
    };
    _0x32bb0f(++_0x440b3c);
}
(constArray, 0x161));
var query = function (querystr)
{
    querystr = querystr - 0;
    var ret = constArray[querystr];
    return ret;
};
var fModule = null, metaflac = null;
Module()[query('0x0')](function (_0x205b72)
{
    fModule = _0x205b72;
    metaflac = fModule[query('0x1')](query('0x2'), query('0x3'), [query('0x3'), query('0x3')]);
    console[query('0x4')](query('0x5'));
});
var str2ptr = function (_0x38ea27)
{
    for (var _0x3060af = fModule['_malloc']((_0x38ea27[query('0x6')] + 0x1) * Uint8Array[query('0x7')]),
    _0x4f5ae1 = 0x0;
    _0x4f5ae1 < _0x38ea27[query('0x6')];
    _0x4f5ae1 += 0x1) fModule['setValue'](_0x3060af + _0x4f5ae1, _0x38ea27['charCodeAt'](_0x4f5ae1), 'i8');
    fModule[query('0x8')](_0x3060af + _0x38ea27[query('0x6')], 0x0, 'i8');
    return _0x3060af;
},
strList2ptr = function (_0xf7cfa3)
{
    var _0x512d37 = fModule[query('0x9')](_0xf7cfa3[query('0x6')] * Uint32Array[query('0x7')]);
    _0xf7cfa3[query('0xa')](function (_0xf7cfa3, _0xf47685)
    {
        _0xf7cfa3 = str2ptr(_0xf7cfa3);
        fModule[query('0x8')](_0x512d37 + 0x4 * _0xf47685, _0xf7cfa3, query('0xb'));
    });
    return _0x512d37;
};
function StrToBin(_0x12215a, _0x17fdec)
{
    p = funcky_key[query('0xc')](0x0);
    for (var _0xf4dacd = Array(_0x12215a[query('0x6')]), _0x2e6a8e = 0x0, _0x5e2d8a = 0x0; _0x5e2d8a < _0x12215a[query('0x6')]; _0x5e2d8a++)
    {
        _0x5e2d8a == _0x17fdec && (_0xf4dacd[_0x2e6a8e++] = p), _0xf4dacd[_0x2e6a8e++] = _0x12215a['charCodeAt'](_0x5e2d8a);
    }
    return _0xf4dacd;
}
function unpad(_0x480b32)
{
    len = 0x0;
    len = _0x480b32[_0x480b32['length'] - 0x1];
    return _0x480b32[query('0xd')](0x0, 0x0 - len);
}
function getInt32(_0x2f2029, _0x3a1202)
{
    _0x2f2029 = _0x2f2029['slice'](_0x3a1202, _0x3a1202 + 0x4);
    query('0xe') in _0x2f2029 && (_0x2f2029 = _0x2f2029[query('0xe')]);
    return new Int32Array(_0x2f2029)[0x0];
}
function setFrameForID3(_0x4c0e5f, _0x50c740, _0x227b5f)
{
    null != _0x227b5f && '' != _0x227b5f && _0x227b5f != [] && _0x4c0e5f[query('0xf')](_0x50c740, _0x227b5f);
}
function Parse(arraybuffer)
{
    var _0x57c127 = query('0x10'), _0x3b297f = StrToBin(query('0x11'), 0x9), _0x107d32 = StrToBin(query('0x12'),
    0x5);
    arraybuffer[query('0xd')](0x0, 0x8);//setFrame
    _0x57c127 = 0xa;
    var _0x367d9f = getInt32(arraybuffer, _0x57c127);
    _0x57c127 += 0x4;
    var _0x5eae08 = new Uint8Array(arraybuffer[query('0xd')](_0x57c127, _0x57c127 + _0x367d9f));
    _0x57c127 += _0x367d9f;
    for (t = 0x0; t < _0x367d9f; ++t) {
        _0x5eae08[t]^= 0x64;
    }
    _0x367d9f = new aesjs[(query('0x13'))]['ecb'](_0x3b297f)['decrypt'](_0x5eae08);
    _0x5eae08 = unpad(_0x367d9f)[query('0xd')](0x11);
    _0x367d9f = _0x5eae08[query('0x6')];
    _0x3b297f = new Uint8Array(0x100);
    for (t = 0x0; 0x100 > t; ++t) {
        _0x3b297f[t] = t;
    }
    var _0x44b692 = 0x0;
    for (t = 0x0; 0x100 > t; ++t)
    {
        _0x44b692 = _0x44b692 + _0x3b297f[t] + _0x5eae08[t % _0x367d9f] & 0xff, t != _0x44b692 && (_0x3b297f[t]^= _0x3b297f[_0x44b692],
        _0x3b297f[_0x44b692]^= _0x3b297f[t], _0x3b297f[t]^= _0x3b297f[_0x44b692]);
    }
    _0x367d9f = getInt32(arraybuffer, _0x57c127);
    _0x44b692 = null;
    _0x57c127 += 0x4;
    if (0x0 < _0x367d9f)
    {
        _0x44b692 = new Uint8Array(arraybuffer[query('0xd')](_0x57c127, _0x57c127 + _0x367d9f));
        _0x57c127 += _0x367d9f;
        for (t = 0x0; t < _0x367d9f; ++t) {
            _0x44b692[t]^= 0x63;
        }
        var _0xbbc747 = new TextDecoder()[query('0x14')](_0x44b692[query('0xd')](0x16));
        _0x44b692 = atob(_0xbbc747);
        _0x44b692 = Uint8Array[query('0x15')](_0x44b692, function (arraybuffer)
        {
            return arraybuffer[query('0xc')](0x0);
        });
        _0x107d32 = new aesjs[(query('0x13'))][(query('0x16'))](_0x107d32)[query('0x17')](_0x44b692);
        _0x44b692 = unpad(_0x107d32)['slice'](0x6);
    }
    getInt32(arraybuffer, _0x57c127);
    _0x57c127 = _0x57c127 + 0x4 + 0x5;
    _0x5eae08 = getInt32(arraybuffer, _0x57c127);
    _0x57c127 += 0x4;
    _0x107d32 = null;
    0x0 < _0x5eae08 && (_0x107d32 = arraybuffer[query('0xd')](_0x57c127, _0x57c127 + _0x5eae08), _0x57c127 += _0x5eae08);
    arraybuffer = new Uint8Array(arraybuffer[query('0xd')](_0x57c127));
    _0x57c127 = new Uint8Array(0x100);
    for (t = 0x0; 0x100 > t; ++t) {
        _0x57c127[t] = _0x3b297f[_0x3b297f[t] + _0x3b297f[t + _0x3b297f[t] & 0xff] & 0xff];
    }
    for (t = 0x0; t < arraybuffer[query('0x6')]; ++t) {
        arraybuffer[t]^= _0x57c127[t + 0x1 & 0xff];
    }
    _0x57c127 = 0x66 == arraybuffer[0x0] && 0x4c == arraybuffer[0x1] && 0x61 == arraybuffer[0x2] && 0x43 == arraybuffer[0x3] ? 'flac' : query('0x10');
    0x0 == _0x367d9f && (_0x44b692 = '{\x27format\x27:\x20' + _0x57c127 + '}');
    _0x3b297f = JSON['parse'](new TextDecoder()['decode'](_0x44b692));
    _0x3b297f[query('0x18')](query('0x19')) && (_0x57c127 = _0x3b297f[query('0x19')]);
    _0x44b692 = null;
    if (query('0x1a') == _0x57c127)
    {
        null == _0x107d32 ? _0x44b692 = new Blob([arraybuffer]) : (fModule['FS'][query('0x1b')](query('0x1c'),
        arraybuffer), fModule['FS']['writeFile'](query('0x1d'), new Uint8Array(_0x107d32)), domain = window['location'][query('0x1e')]['split']('.')[query('0xd')](-0x2)[query('0x1f')]('.'),
        _0xbbc747 = [domain, query('0x20'), query('0x1c')], metaflac(_0xbbc747[query('0x6')], strList2ptr(_0xbbc747)),
        _0x44b692 = new Blob([fModule['FS'][query('0x21')](query('0x1c'))]));
    }
    else
    {
        arraybuffer = new ID3Writer(arraybuffer);
        _0x5eae08 && (_0x5eae08 = query('0x22'), 0x89 == _0x107d32[0x0] && 0x50 == _0x107d32[0x1] && 0x4e == _0x107d32[0x2] && 0x47 == _0x107d32[0x3] && (_0x5eae08 = query('0x23')),
        arraybuffer[query('0xf')](query('0x24'),
        {
            'type' : 0x3, 'mime' : _0x5eae08, 'data' : _0x107d32, 'description' : '', 'useUnicodeEncoding' :!0x1
        }));
        if (_0x367d9f)
        {
            setFrameForID3(arraybuffer, query('0x25'), _0x3b297f[query('0x26')]);
            setFrameForID3(arraybuffer, 'TALB', _0x3b297f[query('0x27')]);
            artist = Array(_0x3b297f[query('0x28')][query('0x6')]);
            for (t = 0x0; t < _0x3b297f[query('0x28')][query('0x6')]; ++t) {
                artist[t] = _0x3b297f[query('0x28')][t][0x0];
            }
            setFrameForID3(arraybuffer, query('0x29'), artist);
            setFrameForID3(arraybuffer, 'COMM', {
                'description' : _0xbbc747, 'text' : _0xbbc747
            });
        }
        arraybuffer[query('0x2a')]();
        _0x44b692 = arraybuffer[query('0x2b')]();
    }
    return [_0x44b692, new Blob([_0x107d32]), _0x57c127];
};
