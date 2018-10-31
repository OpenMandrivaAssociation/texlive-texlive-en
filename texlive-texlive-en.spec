Name:		texlive-texlive-en
Version:	20180527
Release:	2
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
%doc %{_texmfdistdir}/doc/texlive/texlive-en
%doc %{_texmfdistdir}/doc/info/tlbuild.info
%doc %{_texmfdistdir}/doc/texlive/tlbuild

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
