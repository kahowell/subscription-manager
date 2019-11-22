/** Example javascript to make b64 activation key */
function make_b64_activation_key(org, key) {
  return btoa(JSON.stringify({
    'org': org,
    'key': key,
  }));
}

make_b64_activation_key('123', 'foobar')
