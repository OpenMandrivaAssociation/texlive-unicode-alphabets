Name:		texlive-unicode-alphabets
Version:	66225
Release:	1
Summary:	Macros for using characters from Unicode's Private Use Area
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unicode-alphabets
License:	cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unicode-alphabets.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unicode-alphabets.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
While Unicode supports the vast majority of use cases, there
are certain specialized niches which require characters and
glyphs not (yet) represented in the standard. Thus the Private
Use Area (PUA) at code points E000-F8FF, which enables third
parties to define arbitrary character sets. This package allows
configuring a number of macros for using various PUA character
sets in LaTeX (AGL, CYFI, MUFI, SIL, TITUS, UCSUR, UNZ), to
enable transcription and display of medieval and other
documents.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/unicode-alphabets
%doc %{_texmfdistdir}/doc/latex/unicode-alphabets

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
