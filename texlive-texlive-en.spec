# revision 32016
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-en
Version:	20131130
Release:	5
Summary:	TeX Live manual (English)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-en.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-en.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-en package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/texlive/texlive-en/Makefile
%doc %{_texmfdistdir}/doc/texlive/texlive-en/README
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/bv-live.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/bvoutln.sty
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/changemail
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/l.pl
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/live-2003.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/live-2004.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/live-2005.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/live-2007.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/live-2008.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/live-2009.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/live-2010.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/live-2011.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/live-2012.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/live-tl7.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/live4ht.cfg-2004
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/mod.pl
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/nocites.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/picture.tex
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/split.pl
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/status.pl
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/tex-live.bib
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/tex-live.bst
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/tex-live.sty-2003
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/tex-live.sty-2004
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/tex-live.sty-2005
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/tex-live.sty-2007
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/tex-live.sty-2008
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/tex-live.sty-2009
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/tex-live.sty-2010
%doc %{_texmfdistdir}/doc/texlive/texlive-en/archive/texlive.pl
%doc %{_texmfdistdir}/doc/texlive/texlive-en/live4ht.cfg
%doc %{_texmfdistdir}/doc/texlive/texlive-en/tex-live.css
%doc %{_texmfdistdir}/doc/texlive/texlive-en/tex-live.sty
%doc %{_texmfdistdir}/doc/texlive/texlive-en/texlive-en.css
%doc %{_texmfdistdir}/doc/texlive/texlive-en/texlive-en.html
%doc %{_texmfdistdir}/doc/texlive/texlive-en/texlive-en.pdf
%doc %{_texmfdistdir}/doc/texlive/texlive-en/texlive-en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
