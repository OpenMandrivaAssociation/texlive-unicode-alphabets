%global tl_name unicode-alphabets
%global tl_revision 66225

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Macros for using characters from Unicodes Private Use Area
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unicode-alphabets
License:	cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unicode-alphabets.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unicode-alphabets.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
While Unicode supports the vast majority of use cases, there are certain
specialized niches which require characters and glyphs not (yet)
represented in the standard. Thus the Private Use Area (PUA) at code
points E000-F8FF, which enables third parties to define arbitrary
character sets. This package allows configuring a number of macros for
using various PUA character sets in LaTeX (AGL, CYFI, MUFI, SIL, TITUS,
UCSUR, UNZ), to enable transcription and display of medieval and other
documents.

