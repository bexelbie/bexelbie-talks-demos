Notes about how my reveal.js presentations are created and configured.
Eventually a presentation template tool will live here.

# vim-reveal

I have prepared some of my slides using
[`vim-reveal`](https://github.com/blindFS/vim-reveal) a
markdown->reveal.js converter.

The version of `vim-reveal` I am using relies on some unaccepted PRs
that I hope will merge soon.  They are:

* [PR 9](https://github.com/blindFS/vim-reveal/pull/9) - Allowing the
  output directory for the presentation to be changed.
* [PR 7](https://github.com/blindFS/vim-reveal/pull/7) - Allowing slides
  to not require numbering unless nested.
* [PR 8](https://github.com/blindFS/vim-reveal/pull/8) - No new
  functionality, just documentation fixes.

There is also one unsubmitted patch in this branch of my fork:

[bex-dependencies](https://github.com/bexelbie/vim-reveal/tree/bex_dependencies) - Adds allowing additional reveal.js dependencies, but needs work.

These are combined with my custom `vim` configuration and managed with [Vundle](https://github.com/gmarik/Vundle.vim).

```
" git@github.com:bexelbie/vim-reveal.git
" use index.html for output filename
" save the presentation in $CWD
" put reveal one level down
" Set root_path to $CWD
let g:reveal_config = {
            \'filename': 'index',
            \'outputPathDirname': '',
            \'revealWebPath': '..\/tools\/reveal.js\/',
            \'dependencies': '..\/tools\/reveal.js\/plugin\/menu\/menu.js',
            \'path': ''}
Plugin 'bexelbie/vim-reveal'
```

# reveal.js Notes

I use one non-standard plugin as is demonstrated by the dependencies above.

[reveal.js-menu](https://github.com/denehyg/reveal.js-menu) which relies
on one unsubmitted patch in this branch of my fork:

[bex_dir_depth](https://github.com/bexelbie/reveal.js-menu/tree/bex_dir_depth) - Add location awareness for css files but breaks font-awesome when used from localhost but not the web, so it needs work.

# NAQ - Never Asked Questions

1. Why not just use reveal.js?

I wanted to use markdown and the extra lines plus the front matter of
reveal.js seemed to get in the way of my thinking and writing.

2. Why is there only one question?

There is only one question because I couldn't think of two ... oh wait,
I see what you did there.
