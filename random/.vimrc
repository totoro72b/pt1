set nocompatible              " required
filetype off                  " required
set number
set clipboard=unnamed
set encoding=utf-8



" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)


" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" Enable folding
set foldmethod=indent
set foldnestmax=2
set foldlevel=99
set foldlevelstart=0
let g:SimpylFold_docstring_preview = 1
let g:SimpylFold_fold_docstring = 0
let g:SimpylFold_fold_import = 0

" Enable folding with the spacebar
nnoremap <space> za

Plugin 'tmhedberg/SimpylFold'

au BufNewFile,BufRead *.py
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=199 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix |

" au BufNewFile,BufRead *.js, *.html, *.css
"      \ set tabstop=2 |
"      \ set softtabstop=2 |
"      \ set shiftwidth=2 |
"      \ set expandtab |

autocmd Filetype javascript setlocal ts=2 sw=2 expandtab

Plugin 'vim-scripts/indentpython.vim'
highlight BadWhitespace ctermbg=red guibg=darkred
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

"python with virtualenv support
py << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
  project_base_dir = os.environ['VIRTUAL_ENV']
  activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
  execfile(activate_this, dict(__file__=activate_this))
EOF

Plugin 'scrooloose/syntastic'
Plugin 'nvie/vim-flake8'
let python_highlight_all=1
syntax on

Plugin 'scrooloose/nerdtree'

autocmd VimEnter * silent !echo -ne "\033]1337;SetKeyLabel=F7=Flake8\a"
autocmd VimEnter * silent !echo -ne "\033]1337;SetKeyLabel=F1=Help\a"
autocmd VimEnter * silent !echo -ne "\033]1337;SetKeyLabel=F1=NERDTree\a"
autocmd VimLeave * silent !echo -ne "\033]1337;PopKeyLabels\a"
map <silent> <F2> :NERDTreeToggle<CR>

Plugin 'kshenoy/vim-signature'
Plugin 'pangloss/vim-javascript'

" Debug shortcuts
map <silent> <leader>pdb oimport pdb; pdb.set_trace()<esc>
map <silent> <leader>nose ofrom nose.tools import set_trace; set_trace()<esc>
map <silent> <leader>debugger odebugger // eslint-disable-line<esc>

" Make backspace work
set backspace=indent,eol,start

" vim color scheme
Plugin 'flazz/vim-colorschemes'

" Control p
Plugin 'ctrlpvim/ctrlp.vim'
set wildignore+=*/tmp/*,*.so,*.swp,*.zip,*.pyc
let g:ctrlp_user_command = ['.git', 'cd %s && git ls-files -co --exclude-standard']

" indicate this is the window to swap to - max swap
function! MarkWindowSwap()
    let g:markedWinNum = winnr()
endfunction

function! DoWindowSwap()
    "Mark destination
    let curNum = winnr()
    let curBuf = bufnr( "%" )
    exe g:markedWinNum . "wincmd w"
    "Switch to source and shuffle dest->source
    let markedBuf = bufnr( "%" )
    "Hide and open so that we aren't prompted and keep history
    exe 'hide buf' curBuf
    "Switch to dest and shuffle source->dest
    exe curNum . "wincmd w"
    "Hide and open so that we aren't prompted and keep history
    exe 'hide buf' markedBuf
endfunction

nmap <silent> <leader>q :call MarkWindowSwap()<CR>
nmap <silent> <leader>w :call DoWindowSwap()<CR>
