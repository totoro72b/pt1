set nocompatible              " required
filetype off                  " required
set number
set clipboard=unnamed
set encoding=utf-8
filetype plugin indent on    " required
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

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

call vundle#begin()
" ===== Vundle Plugins ======
Plugin 'gmarik/Vundle.vim'
Plugin 'tmhedberg/SimpylFold'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'kshenoy/vim-signature'
Plugin 'pangloss/vim-javascript'
Plugin 'flazz/vim-colorschemes'
Plugin 'ctrlpvim/ctrlp.vim'
Plugin 'w0rp/ale'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
" ===== END OF Vundle Plugins ======
call vundle#end()            " required

" Plug plugins
call plug#begin('~/.vim/plugged')
Plug '/usr/local/opt/fzf'
Plug 'junegunn/fzf.vim'
" Initialize plugin system
call plug#end()

highlight BadWhitespace ctermbg=red guibg=darkred
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

" totoro settings

"
" use comma as the leader key
let mapleader=","
nnoremap fjs :%! python -m json.tool<CR>
" window shortcuts
nnoremap <C-J> <C-W>j
nnoremap <C-K> <C-W>k
nnoremap <C-H> <C-W>h
nnoremap <C-L> <C-W>l
" save stuff
" nnoremap <LEADER>s :update<CR>
" TODO add white space stripping
inoremap <leader>s <ESC>:update<CR>
nnoremap <leader>s :update<CR>
" experimental
nnoremap ; :

" remap tab to escape
 
" escape stuff
inoremap jk <ESC>
inoremap sd <ESC>

" Enable folding
set foldmethod=indent
set foldnestmax=2
set foldlevel=99
set foldlevelstart=0
let g:SimpylFold_docstring_preview = 1
let g:SimpylFold_fold_docstring = 0
let g:SimpylFold_fold_import = 0

" w0rp/ale settings
let g:ale_sign_error = '>>'
let g:ale_sign_warning = '--'

" Enable folding with the spacebar
nnoremap <space> za

let python_highlight_all=1
syntax on

autocmd VimEnter * silent !echo -ne "\033]1337;SetKeyLabel=F7=Flake8\a"
autocmd VimEnter * silent !echo -ne "\033]1337;SetKeyLabel=F1=Help\a"
autocmd VimEnter * silent !echo -ne "\033]1337;SetKeyLabel=F1=NERDTree\a"
autocmd VimLeave * silent !echo -ne "\033]1337;PopKeyLabels\a"
map <silent> <F2> :NERDTreeToggle<CR>

" Debug shortcuts
map <silent> <leader>pdb oimport pdb; pdb.set_trace()<esc>
map <silent> <leader>nose ofrom nose.tools import set_trace; set_trace()<esc>
map <silent> <leader>debugger odebugger // eslint-disable-line<esc>

" Make backspace work
set backspace=indent,eol,start

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

" nmap <silent> <leader>q :call MarkWindowSwap()<CR>
" nmap <silent> <leader>w :call DoWindowSwap()<CR>

" ignore pyc files
let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree
