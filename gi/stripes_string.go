// Code generated by "stringer -type=Stripes"; DO NOT EDIT.

package gi

import (
	"errors"
	"strconv"
)

var _ = errors.New("dummy error")

const _Stripes_name = "NoStripesRowStripesColStripesStripesN"

var _Stripes_index = [...]uint8{0, 9, 19, 29, 37}

func (i Stripes) String() string {
	if i < 0 || i >= Stripes(len(_Stripes_index)-1) {
		return "Stripes(" + strconv.FormatInt(int64(i), 10) + ")"
	}
	return _Stripes_name[_Stripes_index[i]:_Stripes_index[i+1]]
}

func (i *Stripes) FromString(s string) error {
	for j := 0; j < len(_Stripes_index)-1; j++ {
		if s == _Stripes_name[_Stripes_index[j]:_Stripes_index[j+1]] {
			*i = Stripes(j)
			return nil
		}
	}
	return errors.New("String: " + s + " is not a valid option for type: Stripes")
}
