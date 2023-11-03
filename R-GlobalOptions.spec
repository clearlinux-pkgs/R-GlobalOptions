#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-GlobalOptions
Version  : 0.1.2
Release  : 52
URL      : https://cran.r-project.org/src/contrib/GlobalOptions_0.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/GlobalOptions_0.1.2.tar.gz
Summary  : Generate Functions to Get or Set Global Options
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R

%description
and filtering on the values, making options invisible or private.

%prep
%setup -q -c -n GlobalOptions
cd %{_builddir}/GlobalOptions

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641028540

%install
export SOURCE_DATE_EPOCH=1641028540
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library GlobalOptions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library GlobalOptions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library GlobalOptions
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc GlobalOptions || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/GlobalOptions/DESCRIPTION
/usr/lib64/R/library/GlobalOptions/INDEX
/usr/lib64/R/library/GlobalOptions/LICENSE
/usr/lib64/R/library/GlobalOptions/Meta/Rd.rds
/usr/lib64/R/library/GlobalOptions/Meta/features.rds
/usr/lib64/R/library/GlobalOptions/Meta/hsearch.rds
/usr/lib64/R/library/GlobalOptions/Meta/links.rds
/usr/lib64/R/library/GlobalOptions/Meta/nsInfo.rds
/usr/lib64/R/library/GlobalOptions/Meta/package.rds
/usr/lib64/R/library/GlobalOptions/Meta/vignette.rds
/usr/lib64/R/library/GlobalOptions/NAMESPACE
/usr/lib64/R/library/GlobalOptions/NEWS
/usr/lib64/R/library/GlobalOptions/R/GlobalOptions
/usr/lib64/R/library/GlobalOptions/R/GlobalOptions.rdb
/usr/lib64/R/library/GlobalOptions/R/GlobalOptions.rdx
/usr/lib64/R/library/GlobalOptions/doc/GlobalOptions.R
/usr/lib64/R/library/GlobalOptions/doc/GlobalOptions.Rmd
/usr/lib64/R/library/GlobalOptions/doc/GlobalOptions.html
/usr/lib64/R/library/GlobalOptions/doc/index.html
/usr/lib64/R/library/GlobalOptions/help/AnIndex
/usr/lib64/R/library/GlobalOptions/help/GlobalOptions.rdb
/usr/lib64/R/library/GlobalOptions/help/GlobalOptions.rdx
/usr/lib64/R/library/GlobalOptions/help/aliases.rds
/usr/lib64/R/library/GlobalOptions/help/paths.rds
/usr/lib64/R/library/GlobalOptions/html/00Index.html
/usr/lib64/R/library/GlobalOptions/html/R.css
/usr/lib64/R/library/GlobalOptions/tests/test-all.R
/usr/lib64/R/library/GlobalOptions/tests/testthat/test.R
