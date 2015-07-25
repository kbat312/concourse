require 'test/unit'
require 'concourse'

class TestUtils < Test::Unit::TestCase

    def test_convert_string_round_trip
        orig = "foo"
        assert_equal(orig, Concourse::Utils::Convert::thrift_to_ruby(Concourse::Utils::Convert::ruby_to_thrift(orig)))
    end

    def test_convert_tag_round_trip
        orig = Concourse::Tag.create "foo"
        assert_equal(orig, Concourse::Utils::Convert::thrift_to_ruby(Concourse::Utils::Convert::ruby_to_thrift(orig)))
    end

    def test_convert_link_round_trip
        orig = Concourse::Link.to 2147483648
        assert_equal(orig, Concourse::Utils::Convert::thrift_to_ruby(Concourse::Utils::Convert::ruby_to_thrift(orig)))
    end

    def test_convert_int_round_trip
        orig = 10
        assert_equal(orig, Concourse::Utils::Convert::thrift_to_ruby(Concourse::Utils::Convert::ruby_to_thrift(orig)))
    end

    def test_convert_long_round_trip
        orig = 2147483649
        assert_equal(orig, Concourse::Utils::Convert::thrift_to_ruby(Concourse::Utils::Convert::ruby_to_thrift(orig)))
    end

    def test_convert_boolean_round_trip
        orig = false
        assert_equal(orig, Concourse::Utils::Convert::thrift_to_ruby(Concourse::Utils::Convert::ruby_to_thrift(orig)))
    end

    def test_convert_float_round_trip
        orig = 3.14353
        assert_equal(orig, Concourse::Utils::Convert::thrift_to_ruby(Concourse::Utils::Convert::ruby_to_thrift(orig)))
    end

end
