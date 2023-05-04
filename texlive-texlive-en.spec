Name:		texlive-texlive-en
Version:	66914
Release:	1
Summary:	TeX Live manual (English)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-en.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-en.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
